# https://gist.github.com/mongoose54/c93c113ae195188394a7b363c24e2ac0#file-gistfile1-txt

from __future__ import division, print_function
import sys
import os
from collections import OrderedDict
import logging
import shutil

import numpy as np
import tensorflow as tf
import minitest

sys.path.append("..")
from tf_unet import image_gen
from tf_unet import util


logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

def crop_and_concat(x1,x2):
    x1_shape = tf.shape(x1)
    x2_shape = tf.shape(x2)
    # offsets for the top left corner of the crop
    offsets = [0, (x1_shape[1] - x2_shape[1]) // 2, (x1_shape[2] - x2_shape[2]) // 2, 0]
    size = [-1, x2_shape[1], x2_shape[2], -1]
    x1_crop = tf.slice(x1, offsets, size)
    # change for tf 1.0
    # return tf.concat(3, [x1_crop, x2])
    return tf.concat([x1_crop, x2], 3)

def create_unet(channels=3, n_class=2, layers=3, features_root=16, **kwargs):
    filter_size = kwargs.get("filter_size", 3)
    pool_size = kwargs.get("pool_size", 2)
    summaries = kwargs.get("summaries", True)

    # Remove nodes from graph or reset entire default graph
    tf.reset_default_graph()
        
    with tf.name_scope('input'):
        x = tf.placeholder(tf.float32, name='x-input',
                shape=[None, None, None, channels])
        y = tf.placeholder(tf.float32, name='y-input', 
                shape=[None, None, None, n_class])

    # summary move
    keep_prob = tf.placeholder(tf.float32)

    
    # logits, self.variables, self.offset = 
    # create_conv_net(self.x, self.keep_prob, channels, n_class, **kwargs)

    # Notice: in_node is same as x, no different, 
    logging.info(("Layers {0}, features {1}, filter size "+
            "{2}x{2}, pool size: {3}x{3}").format(
            layers,features_root, filter_size, pool_size))    

    # since channels always equal tf.shape(x)[3]
    in_node = tf.reshape(x, tf.stack(
            [-1,tf.shape(x)[1],tf.shape(x)[2],channels]))
    batch_size = tf.shape(in_node)[0]
 
    weights = []
    biases = []
    # convs = []
    # pools = OrderedDict()
    # deconv = OrderedDict()
    dw_h_convs = OrderedDict()
    up_h_convs = OrderedDict()
    
    in_size = 1000
    size = in_size
    # down layers
    for layer in range(0, layers):
        features = 2**layer*features_root
        stddev = np.sqrt(2 / (filter_size**2 * features))

            
        if layer == 0:
            w1 = tf.Variable(tf.truncated_normal([filter_size, filter_size, channels, features], stddev))
        else:
            w1 = tf.Variable(tf.truncated_normal([filter_size, filter_size, features//2, features], stddev))
        w2 = tf.Variable(tf.truncated_normal([filter_size, filter_size, features, features], stddev))

        b1 = tf.Variable(tf.constant(0.1, shape=[features]))
        b2 = tf.Variable(tf.constant(0.1, shape=[features]))
        

        conv1 = tf.nn.conv2d(in_node, w1, strides=[1, 1, 1, 1], padding='VALID')
        conv1_dropout = tf.nn.dropout(conv1, keep_prob)
        tmp_h_conv = tf.nn.relu(conv1_dropout + b1)

        conv2 = tf.nn.conv2d(tmp_h_conv, w2, strides=[1, 1, 1, 1], padding='VALID')
        conv2_dropout = tf.nn.dropout(conv2, keep_prob)
        dw_h_convs[layer] = tf.nn.relu(conv2_dropout + b2)
        
        weights.append((w1, w2))
        biases.append((b1, b2))
        # convs.append((conv1_dropout, conv2_dropout))
        
        size -= 4
        if layer < layers-1:
            # print("some:",layer)P
            in_node = tf.nn.max_pool(dw_h_convs[layer], 
                    ksize=[1, pool_size, pool_size, 1], strides=[1, pool_size, pool_size, 1], 
                    padding='VALID')
            size /= 2
        
    in_node = dw_h_convs[layers-1]
        

    # up layers
    for layer in range(layers-2, -1, -1):
        features = 2**(layer+1)*features_root
        stddev = np.sqrt(2 / (filter_size**2 * features))
        
        wd = tf.Variable(tf.truncated_normal([pool_size, pool_size, features//2, features], stddev))
        bd = tf.Variable(tf.constant(0.1, shape=[features//2]))


        x_shape = tf.shape(in_node)
        output_shape = tf.stack([x_shape[0], x_shape[1]*2, x_shape[2]*2, x_shape[3]//2])
        h_deconv = tf.nn.conv2d_transpose(in_node, wd, output_shape, strides=[1, pool_size, pool_size, 1], padding='VALID')
        h_deconv_relu = tf.nn.relu(h_deconv + bd)
        h_deconv_concat = crop_and_concat(dw_h_convs[layer], h_deconv_relu)
        # deconv[layer] = h_deconv_concat
        
        w1 = tf.Variable(tf.truncated_normal([filter_size, filter_size, features, features//2], stddev))
        w2 = tf.Variable(tf.truncated_normal([filter_size, filter_size, features//2, features//2], stddev))
        b1 = tf.Variable(tf.constant(0.1, shape=[features//2]))
        b2 = tf.Variable(tf.constant(0.1, shape=[features//2]))
        
        conv1 = tf.nn.conv2d(h_deconv_concat, w1, strides=[1, 1, 1, 1], padding='VALID')
        conv1_dropout = tf.nn.dropout(conv1, keep_prob)
        h_conv = tf.nn.relu(conv1_dropout + b1)

        conv2 = tf.nn.conv2d(h_conv, w2, strides=[1, 1, 1, 1], padding='VALID')
        conv2_dropout = tf.nn.dropout(conv2, keep_prob)
        in_node = tf.nn.relu(conv2_dropout + b2)
        up_h_convs[layer] = in_node
    
        weights.append((w1, w2))
        biases.append((b1, b2))
        # convs.append((conv1_dropout, conv2_dropout))
        
        size *= 2
        size -= 4

    # Output Map
    weight = tf.Variable(tf.truncated_normal([1, 1, features_root, n_class], stddev))
    bias = tf.Variable(tf.constant(0.1, shape=[n_class]))
    conv = tf.nn.conv2d(in_node, weight, strides=[1, 1, 1, 1], padding='VALID')
    conv_dropout = tf.nn.dropout(conv, tf.constant(1.0))
    output_map = tf.nn.relu(conv_dropout + bias)
    up_h_convs["out"] = output_map

    variables = []
    for w1,w2 in weights:
        variables.append(w1)
        variables.append(w2)
        
    for b1,b2 in biases:
        variables.append(b1)
        variables.append(b2)

    # import ipdb; ipdb.set_trace()
    return {"logits":output_map,"weights_biases":variables,
            "x":x, "y":y, "keep_prob":keep_prob}


    # return output_map, variables#, int(in_size - size)

    # self.cost = self._get_cost(output_map, cost, cost_kwargs)
    
    # self.gradients_node = tf.gradients(self.cost, self.variables)
     
    # self.cross_entropy = tf.reduce_mean(cross_entropy(
    #         tf.reshape(self.y, [-1, n_class]),
    #         tf.reshape(pixel_wise_softmax_2(output_map), [-1, n_class])))
    
    # self.predicter = pixel_wise_softmax_2(output_map)
    # self.correct_pred = tf.equal(tf.argmax(self.predicter, 3), tf.argmax(self.y, 3))
    # self.accuracy = tf.reduce_mean(tf.cast(self.correct_pred, tf.float32))

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
                class_weights = tf.constant(np.array(class_weights, dtype=np.float32))
        
                weight_map = tf.mul(flat_labels, class_weights)
                weight_map = tf.reduce_sum(weight_map, axis=1)
        
                # loss_map = tf.nn.softmax_cross_entropy_with_logits(flat_logits, flat_labels)
                loss_map = tf.nn.softmax_cross_entropy_with_logits(logits=flat_logits, 
                                                                    labels=flat_labels)
                weighted_loss = tf.mul(loss_map, weight_map)
        
                loss = tf.reduce_mean(weighted_loss)
                
            else:
                # loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(flat_logits, 
                #                                                               flat_labels))
                # change for tf 1.0
                loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=flat_logits, 
                                                                              labels=flat_labels))
        elif cost_name == "dice_coefficient":
            intersection = tf.reduce_sum(flat_logits * flat_labels, axis=1, keep_dims=True)
            union = tf.reduce_sum(tf.mul(flat_logits, flat_logits), axis=1, keep_dims=True) \
                    + tf.reduce_sum(tf.mul(flat_labels, flat_labels), axis=1, keep_dims=True)
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
            learning_rate_node = tf.Variable(learning_rate)
            
            optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate_node, 
                    **optimizer_options).minimize(cost,global_step=global_step)
        
        return optimizer, learning_rate_node

    @staticmethod
    def _pixel_wise_softmax_2(output_map):
        exponential_map = tf.exp(output_map)
        sum_exp = tf.reduce_sum(exponential_map, 3, keep_dims=True)
        tensor_sum_exp = tf.tile(sum_exp, tf.stack([1, 1, 1, tf.shape(output_map)[3]]))
        return tf.div(exponential_map,tensor_sum_exp)

    @staticmethod
    def _error_rate(predictions, labels):
        """
        Return the error rate based on dense predictions and 1-hot labels.
        """
        
        return 100.0 - (
            100.0 *
            np.sum(np.argmax(predictions, 3) == np.argmax(labels, 3)) /
            (predictions.shape[0]*predictions.shape[1]*predictions.shape[2]))


    @staticmethod
    def _store_prediction(sess, batch_x, batch_y, name, predicter, prediction_path, cost, x, y, keep_prob):
        prediction = sess.run(predicter, 
                feed_dict={x: batch_x, y: batch_y, keep_prob: 1.})
        pred_shape = prediction.shape
        
        loss = sess.run(cost, feed_dict={x: batch_x, 
                y: util.crop_to_shape(batch_y, pred_shape), keep_prob: 1.})
        
        logging.info("Verification error= {:.1f}%, loss= {:.4f}".format(
                Trainer._error_rate(prediction, util.crop_to_shape(batch_y,
                prediction.shape)), loss))
              
        img = util.combine_img_prediction(batch_x, batch_y, prediction)
        util.save_image(img, "%s/%s.jpg"%(prediction_path, name))
        
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
        kwargs.p()
        output_path = kwargs.get("output_path")
        n_class = kwargs.get("n_class")
        batch_size =kwargs.get("batch_size", 1)
        # training_iters =kwargs.get("training_iters", 10)
        training_iters =kwargs.get("training_iters", 1)
        epochs =kwargs.get("epochs", 100)
        dropout =kwargs.get("dropout", 0.75)
        display_step =kwargs.get("display_step", 5)
        is_restore =kwargs.get("is_restore", False)
        cost_options =kwargs.get("cost_options", {})
        optimizer_options =kwargs.get("optimizer_options", {"type":"momentum"})

        logits = unet_hash["logits"]
        weights_biases = unet_hash["weights_biases"]
        x = unet_hash["x"]
        y = unet_hash["y"]
        keep_prob = unet_hash["keep_prob"]

        prediction_path = "prediction"
        verification_batch_size = 4

        Trainer._clear_path(prediction_path, output_path, is_restore)
        cost = Trainer._get_cost(logits,weights_biases,
                y, n_class, cost_options)
        
        gradients_node = tf.gradients(cost, weights_biases)
        # gradients_node.size().p()
        # weights_biases.size().p()

        norm_gradients_node = tf.Variable(tf.constant(0.0, shape=[len(gradients_node)]))
        
        global_step = tf.Variable(0)
        optimizer, learning_rate_node = Trainer._get_optimizer(
                training_iters, global_step, cost, optimizer_options)

        cross_entropy = -tf.reduce_mean(tf.reshape(y, [-1, n_class])*
                tf.log(tf.clip_by_value(tf.reshape(
                Trainer._pixel_wise_softmax_2(logits), [-1, n_class]),
                1e-10,1.0)), name="cross_entropy")
        
        predicter = Trainer._pixel_wise_softmax_2(logits)
        correct_pred = tf.equal(tf.argmax(predicter, 3), tf.argmax(y, 3))
        accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

        # # if self.net.summaries:
        # #     tf.summary.histogram('norm_grads', self.norm_gradients_node)

        tf.summary.scalar('loss', cost)
        tf.summary.scalar('cross_entropy', cross_entropy)
        tf.summary.scalar('accuracy', accuracy)

        tf.summary.scalar('learning_rate', learning_rate_node)

        summary_op = tf.summary.merge_all()        
        init = tf.global_variables_initializer()
        
        
        save_path = os.path.join(output_path, "model.cpkt")
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
                for step in range((epoch*training_iters), ((epoch+1)*training_iters)):
                    batch_x, batch_y = data_provider(batch_size)
                     
                    # Run optimization op (backprop)
                    _, loss, lr, gradients = sess.run(
                            (optimizer, cost, learning_rate_node, gradients_node), 
                            feed_dict={x: batch_x, y: util.crop_to_shape(batch_y, pred_shape),
                            keep_prob: dropout})

                    if avg_gradients is None:
                        avg_gradients = [np.zeros_like(gradient) for gradient in gradients]
                    for i in range(len(gradients)):
                        avg_gradients[i] = (avg_gradients[i] * 
                                (1.0 - (1.0 / (step+1)))) + (gradients[i] / (step+1))
                        
                    norm_gradients = [np.linalg.norm(gradient) for gradient in avg_gradients]
                    norm_gradients_node.assign(norm_gradients).eval()
                    
                    if step % display_step == 0:
                        new_batch_y = util.crop_to_shape(batch_y, pred_shape)
                        summary_str, loss, acc, predictions = sess.run(
                                [summary_op, cost, accuracy, predicter], 
                                feed_dict={x: batch_x, y: new_batch_y,
                                keep_prob: 1.})
                        # summary_writer.add_summary(summary_str, step)
                        # summary_writer.flush()
                        logging.info("Iter {:}, Minibatch Loss= {:.4f}, Training Accuracy= {:.4f}, Minibatch error= {:.1f}%".format(
                                step, loss, acc, Trainer._error_rate(predictions, new_batch_y)))

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

def predict(predicter, unet_hash, x_test, n_class, model_path):
    """
    Uses the model to create a prediction for the given data
    
    :param model_path: path to the model checkpoint to restore
    :param x_test: Data to predict on. Shape [n, nx, ny, channels]
    :returns prediction: The unet prediction Shape [n, px, py, labels] (px=nx-self.offset/2) 
    """
    
    init = tf.global_variables_initializer()
    with tf.Session() as sess:
        # Initialize variables
        sess.run(init)
    
        # Restore model weights from previously saved model
        _restore(sess, model_path)
        
        y_dummy = np.empty((x_test.shape[0], x_test.shape[1], x_test.shape[2], n_class))
        prediction = sess.run(predicter, feed_dict={unet_hash["x"]: x_test, 
                unet_hash["y"]: y_dummy, unet_hash["keep_prob"]: 1.})
        
    return prediction

# def toy_problem():
#     nx = 572
#     ny = 572
#     generator = image_gen.GrayScaleDataProvider(nx, ny, cnt=20)
#     x_test, y_test = generator(4)
#     # generator.channels 1
#     # generator.n_class 2

#     unet_hash = create_unet(channels=generator.channels, n_class=generator.n_class, layers=3, features_root=16)
#     train_kwargs = {"output_path":"./unet_trained", 
#         "n_class":generator.n_class,
#         "cost_options":{"type":"cross_entropy"},
#         "optimizer_options":{"type":"momentum"},
#         "epochs":1
#         }

#     predicter = Trainer.do(unet_hash, generator, **train_kwargs)
#     prediction = predict(predicter, unet_hash, x_test, generator.n_class, "./unet_trained/model.cpkt")
        


# toy_problem()
# print("ok")


