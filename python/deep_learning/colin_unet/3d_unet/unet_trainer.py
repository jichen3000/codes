from __future__ import division, print_function
import sys
import os
from collections import OrderedDict
import logging
import shutil

import numpy as np
import tensorflow as tf
import minitest

# sys.path.append("..")
# from tf_unet import image_gen
# from tf_unet import util


logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

# def crop_to_shape(data, shape):
#     print("crop_to_shape")
#     if data.shape[1:] == shape[1:]:
#         print("crop_to_shape:same")
#         return data
#     """
#     Crops the array to the given image shape by removing the border (expects a tensor of shape [batches, nx, ny, channels].
    
#     :param data: the array to crop
#     :param shape: the target shape
#     """
#     if len(shape) == 4:
#         offset0 = (data.shape[1] - shape[1])//2
#         offset1 = (data.shape[2] - shape[2])//2
#         return data[:, offset0:(-offset0), offset1:(-offset1)]
#     if len(shape) == 5:
#         offset0 = (data.shape[1] - shape[1])//2
#         offset1 = (data.shape[2] - shape[2])//2
#         offset2 = (data.shape[3] - shape[3])//2
#         return data[:, offset0:(-offset0), offset1:(-offset1), offset2:(-offset2)]


class Trainer(object):
                    
    @staticmethod
    def _clear_path(prediction_path, output_path, is_restore):
        
        
        prediction_path = os.path.abspath(prediction_path)
        output_path = os.path.abspath(output_path)
        
        if not is_restore:
            logging.info("Removing '{:}'".format(prediction_path))
            shutil.rmtree(prediction_path, ignore_errors=True)
            logging.info("Removing '{:}'".format(output_path))
            shutil.rmtree(output_path, ignore_errors=True)
        
        if not os.path.exists(prediction_path):
            logging.info("Allocating '{:}'".format(prediction_path))
            os.makedirs(prediction_path)
        
        if not os.path.exists(output_path):
            logging.info("Allocating '{:}'".format(output_path))
            os.makedirs(output_path)
        
    @staticmethod
    def _get_cost(logits, weights_biases, y, n_class, cost_kwargs):
        """
        Constructs the cost function, either cross_entropy, weighted cross_entropy or dice_coefficient.
        Optional arguments are: 
        class_weights: weights for the different classes in case of multi-class imbalance
        regularizer: power of the L2 regularizers added to the loss function
        """
        cost_name = cost_kwargs.get("type","cross_entropy")
        
        flat_logits = tf.reshape(logits, [-1, n_class])
        flat_labels = tf.reshape(y, [-1, n_class])
        if cost_name == "cross_entropy":
            class_weights = cost_kwargs.pop("class_weights", None)
            
            if class_weights is not None:
                logging.info("useing class_weights")
                class_weights = tf.constant(np.array(class_weights, dtype=np.float32))
        
                weight_map = tf.multiply(flat_labels, class_weights)
                weight_map = tf.reduce_sum(weight_map, axis=1)
        
                # loss_map = tf.nn.softmax_cross_entropy_with_logits(flat_logits, flat_labels)
                loss_map = tf.nn.softmax_cross_entropy_with_logits(logits=flat_logits, 
                                                                    labels=flat_labels)
                weighted_loss = tf.multiply(loss_map, weight_map)
        
                loss = tf.reduce_mean(weighted_loss)
                
            else:
                # loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(flat_logits, 
                #                                                               flat_labels))
                # change for tf 1.0
                # logging.info("use this")
                loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=flat_logits, 
                                                                              labels=flat_labels))
        elif cost_name == "dice_coefficient":
            intersection = tf.reduce_sum(flat_logits * flat_labels, axis=1, keep_dims=True)
            union = tf.reduce_sum(tf.multiply(flat_logits, flat_logits), axis=1, keep_dims=True) \
                    + tf.reduce_sum(tf.multiply(flat_labels, flat_labels), axis=1, keep_dims=True)
            loss = 1 - tf.reduce_mean(2 * intersection/ (union))
        else:
            raise ValueError("Unknown cost function: "%cost_name)

        regularizer = cost_kwargs.pop("regularizer", None)
        if regularizer is not None:
            regularizers = sum([tf.nn.l2_loss(variable) for variable in weights_biases])
            loss += (regularizer * regularizers)
            
        return loss

    @staticmethod
    def _get_optimizer(training_iters, global_step, cost, optimizer_options):
        the_type = optimizer_options.pop("type", "momentum")
        # the_type = optimizer_options.pop("type", "adam")
        logging.info("optimizer using "+the_type)
        if the_type == "momentum":
            learning_rate = optimizer_options.pop("learning_rate", 0.2)
            decay_rate = optimizer_options.pop("decay_rate", 0.95)
            momentum = optimizer_options.pop("momentum", 0.2)
            
            learning_rate_node = tf.train.exponential_decay(
                    learning_rate=learning_rate, 
                    global_step=global_step, 
                    decay_steps=training_iters,  
                    decay_rate=decay_rate, 
                    staircase=True)
            
            optimizer = tf.train.MomentumOptimizer(learning_rate=learning_rate_node, 
                    momentum=momentum, **optimizer_options).minimize(
                    cost, global_step=global_step)
        elif the_type == "adam":
            learning_rate = optimizer_options.pop("learning_rate", 0.001)
            # decay_rate = optimizer_options.pop("decay_rate", 0.2)
            # learning_rate_node = tf.train.exponential_decay(
            #         learning_rate=learning_rate, 
            #         global_step=global_step, 
            #         decay_steps=training_iters,  
            #         decay_rate=decay_rate, 
            #         staircase=True)
            learning_rate_node = tf.Variable(learning_rate)
            
            optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate_node, 
                    **optimizer_options).minimize(cost,global_step=global_step)
        
        return optimizer, learning_rate_node

    @staticmethod
    def _pixel_wise_softmax_2(output_map):
        return tf.nn.softmax(output_map)
        # this will cause, result has np.nan
        # exponential_map = tf.exp(output_map)
        # sum_exp = tf.reduce_sum(exponential_map, 4, keep_dims=True)
        # tensor_sum_exp = tf.tile(sum_exp, tf.stack([1, 1, 1, 1, tf.shape(output_map)[4]]))
        # return tf.div(exponential_map,tensor_sum_exp)

    @staticmethod
    def _error_rate(predictions, labels):
        """
        Return the error rate based on dense predictions and 1-hot labels.
        """
        the_shape = predictions.shape
        last_dim = len(the_shape) - 1
        count = reduce(lambda x,y: x * y, the_shape[:-1])
        # np.argmax(predictions, last_dim) is all zeros, since predictions is all 0.5
        p_max = np.argmax(predictions, last_dim)
        same_count = np.sum(p_max == np.argmax(labels, last_dim))
        # [predictions.min(),predictions.max()].p()
        np.unique(predictions[...,0], return_counts=True).p()
        if np.count_nonzero(p_max) == 0:
            same_count = 0
        # import ipdb; ipdb.set_trace()
        return 100.0 - (100.0 *  same_count/ count)


    @staticmethod
    def _store_prediction(sess, batch_x, batch_y, name, predicter, prediction_path, cost, x, y, keep_prob):
        prediction = sess.run(predicter, 
                feed_dict={x: batch_x, y: batch_y, keep_prob: 1.})
        # logits_value = sess.run(logits, feed_dict={x: batch_x, y: batch_y, keep_prob: 1.})
        pred_shape = prediction.shape
        
        # cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=flat_logits, 
                   
        # cur_y = crop_to_shape(batch_y, pred_shape) 
        loss = sess.run(cost, feed_dict={x: batch_x, 
                y: batch_y, keep_prob: 1.})
        
        logging.info("Verification error= {:.1f}%, loss= {:.4f}".format(
                Trainer._error_rate(prediction, batch_y), loss))
              
        # not for 3d
        # img = util.combine_img_prediction(batch_x, batch_y, prediction)
        # util.save_image(img, "%s/%s.jpg"%(prediction_path, name))
        
        return pred_shape

    @staticmethod
    def _output_epoch_stats(epoch, total_loss, training_iters, lr):
        logging.info("Epoch {:}, Average loss: {:.4f}, learning rate: {:.4f}".format(
                epoch, (total_loss / training_iters), lr))
    
    # @staticmethod
    # def _output_minibatch_stats(sess, step, batch_x, batch_y, summary_writer=None):
    #     # Calculate batch loss and accuracy
    #     # summary_str, loss, acc, predictions = sess.run([self.summary_op, 
    #     #                                                     self.net.cost, 
    #     #                                                     self.net.accuracy, 
    #     #                                                     self.net.predicter], 
    #     #                                                    feed_dict={self.net.x: batch_x,
    #     #                                                               self.net.y: batch_y,
    #     #                                                               self.net.keep_prob: 1.})
    #     # summary_writer.add_summary(summary_str, step)
    #     # summary_writer.flush()
    #     logging.info("Iter {:}, Minibatch Loss= {:.4f}, Training Accuracy= {:.4f}, Minibatch error= {:.1f}%".format(
    #             step, loss, acc, error_rate(predictions, batch_y)))

    @staticmethod
    def _save(sess, model_path):
        """
        Saves the current session to a checkpoint
        
        :param sess: current session
        :param model_path: path to file system location
        """
        
        saver = tf.train.Saver()
        save_path = saver.save(sess, model_path)
        return save_path

    @staticmethod
    def do(unet_hash, data_provider, **kwargs):
        """
        Lauches the training process
        
        :param data_provider: callable returning training and verification data
        :param output_path: path where to store checkpoints
        :param training_iters: number of training mini batch iteration
        :param epochs: number of epochs
        :param dropout: dropout probability
        :param display_step: number of steps till outputting stats
        :param restore: Flag if previous model should be restored 
        """
        # kwargs.p()
        output_path = kwargs.get("output_path")
        n_class = kwargs.get("n_class")
        batch_size =kwargs.get("batch_size", 1)
        training_iters =kwargs.get("training_iters", 10)
        # training_iters =kwargs.get("training_iters", 1)
        epochs =kwargs.get("epochs", 100)
        dropout =kwargs.get("dropout", 0.75)
        display_step =kwargs.get("display_step", 5)
        is_restore =kwargs.get("is_restore", False)
        verification_batch_size =kwargs.get("verification_batch_size", 4)
        prediction_path =kwargs.get("prediction_path", "prediction")
        cost_options =kwargs.get("cost_options", {})
        optimizer_options =kwargs.get("optimizer_options", {"type":"momentum"})

        logits = unet_hash["logits"]
        weights_biases = unet_hash["weights_biases"]
        x = unet_hash["x"]
        y = unet_hash["y"]
        keep_prob = unet_hash["keep_prob"]


        predicter = Trainer._pixel_wise_softmax_2(logits)
        logging.info("new predicter = tf.nn.softmax(logits)")

        Trainer._clear_path(prediction_path, output_path, is_restore)
        cost = Trainer._get_cost(logits,weights_biases,
                y, n_class, cost_options)
        # cost = Trainer._get_cost(predicter,weights_biases,
        #         y, n_class, cost_options)
        
        gradients_node = tf.gradients(cost, weights_biases)

        norm_gradients_node = tf.Variable(tf.constant(0.0, shape=[len(gradients_node)]))
        
        global_step = tf.Variable(0)
        optimizer, learning_rate_node = Trainer._get_optimizer(
                training_iters, global_step, cost, optimizer_options)

        # cross_entropy = -tf.reduce_mean(tf.reshape(y, [-1, n_class])*
        #         tf.log(tf.clip_by_value(tf.reshape(
        #         Trainer._pixel_wise_softmax_2(logits), [-1, n_class]),
        #         1e-10,1.0)), name="cross_entropy")
        
        correct_pred = tf.equal(tf.argmax(predicter, 4), tf.argmax(y, 4))
        accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

        # # if self.net.summaries:
        # #     tf.summary.histogram('norm_grads', self.norm_gradients_node)

        # tf.summary.scalar('loss', cost)
        # tf.summary.scalar('cross_entropy', cross_entropy)
        # tf.summary.scalar('accuracy', accuracy)

        tf.summary.scalar('learning_rate', learning_rate_node)

        summary_op = tf.summary.merge_all()        
        init = tf.global_variables_initializer()
        
        
        save_path = os.path.join(output_path, "model.cpkt")
        # sess = tf.Session()
        with tf.Session() as sess:
            sess.run(init)
            
            if is_restore:
                ckpt = tf.train.get_checkpoint_state(output_path)
                if ckpt and ckpt.model_checkpoint_path:
                    _restore(sess, ckpt.model_checkpoint_path)
            
            test_x, test_y = data_provider(verification_batch_size)
            name = "_init"
            pred_shape = Trainer._store_prediction(sess, test_x, test_y, name, 
                    predicter, prediction_path, cost, x, y, keep_prob)
            
            # summary_writer = tf.summary.FileWriter(output_path, graph=sess.graph)

            logging.info("Start optimization")
            avg_gradients = None

            for epoch in range(epochs):
                total_loss = 0
                # epoch.p()
                for step in range((epoch*training_iters), ((epoch+1)*training_iters)):
                    # step.p()
                    batch_x, batch_y = data_provider(batch_size)
                    # batch_y[...,1].sum().p()
                     
                    # new_batch_y_1 = crop_to_shape(batch_y, pred_shape)
                    # batch_y.shape.p()
                    # new_batch_y_1.shape.p()
                    # pred_shape.p()

                    # Run optimization op (backprop)
                    _, loss, lr, gradients = sess.run(
                            # (optimizer, cost, learning_rate_node, norm_gradients_node), 
                            (optimizer, cost, learning_rate_node, gradients_node), 
                            feed_dict={x: batch_x, y: batch_y,
                            keep_prob: dropout})

                    # gradients[0].sum().p()
                    # import ipdb; ipdb.set_trace()

                    if avg_gradients is None:
                        avg_gradients = [np.zeros_like(gradient) for gradient in gradients]
                    for i in range(len(gradients)):
                        avg_gradients[i] = (avg_gradients[i] * 
                                (1.0 - (1.0 / (step+1)))) + (gradients[i] / (step+1))
                        
                    norm_gradients = [np.linalg.norm(gradient) for gradient in avg_gradients]
                    norm_gradients_node.assign(norm_gradients).eval()
                    
                    if step % display_step == 0:
                        # new_batch_y = crop_to_shape(batch_y, pred_shape)
                        summary_str, loss, acc, predictions = sess.run(
                                [summary_op, cost, accuracy, predicter], 
                                feed_dict={x: batch_x, y: batch_y,
                                keep_prob: 1.})
                        # summary_writer.add_summary(summary_str, step)
                        # summary_writer.flush()
                        # [predictions.min(), predictions.max()].p()
                        logging.info("Iter {:}, Minibatch Loss= {:.4f}, Training Accuracy= {:.4f}, Minibatch error= {:.1f}%".format(
                                step, loss, acc, Trainer._error_rate(predictions, batch_y)))

                    total_loss += loss

                Trainer._output_epoch_stats(epoch, total_loss, training_iters, lr)
                Trainer._store_prediction(sess, test_x, test_y, "epoch_%s"%epoch, 
                        predicter, prediction_path, cost, x, y, keep_prob)
                    
                save_path = Trainer._save(sess, save_path)
            logging.info("Optimization Finished!")
            
        return predicter

def _restore(sess, model_path):
    """
    Restores a session from a checkpoint
    
    :param sess: current session instance
    :param model_path: path to file system checkpoint location
    """
    
    saver = tf.train.Saver()
    saver.restore(sess, model_path)
    logging.info("Model restored from file: %s" % model_path)

def predict(unet_hash, x_test, n_class, model_path):
    """
    Uses the model to create a prediction for the given data
    
    :param model_path: path to the model checkpoint to restore
    :param x_test: Data to predict on. Shape [n, nx, ny, channels]
    :returns prediction: The unet prediction Shape [n, px, py, labels] (px=nx-self.offset/2) 
    """
    logits = unet_hash["logits"]
    x = unet_hash["x"]
    y = unet_hash["y"]
    keep_prob = unet_hash["keep_prob"]
    predicter = Trainer._pixel_wise_softmax_2(logits)

    init = tf.global_variables_initializer()
    with tf.Session() as sess:
        # Initialize variables
        sess.run(init)
    
        # Restore model weights from previously saved model
        _restore(sess, model_path)
        
        y_dummy = np.empty((x_test.shape[0], x_test.shape[1], x_test.shape[2], x_test.shape[3], n_class))
        prediction = sess.run(predicter, feed_dict={x: x_test, 
                y: y_dummy, keep_prob: 1.})
        
    return prediction

