from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import sys

from tensorflow.examples.tutorials.mnist import input_data

import tensorflow as tf
import numpy as np

def train_and_save():
    data_dir = "./data"
    mnist = input_data.read_data_sets(data_dir, one_hot=True)

    # Create the model
    x = tf.placeholder(tf.float32, [None, 784], name="x")
    W = tf.Variable(tf.zeros([784, 10]), name="W")
    b = tf.Variable(tf.zeros([10]), name="b")
    with tf.name_scope('y'):
        y = tf.matmul(x, W) + b

    # Define loss and optimizer
    y_ = tf.placeholder(tf.float32, [None, 10], name="y_")

    cross_entropy = tf.reduce_mean(
            tf.nn.softmax_cross_entropy_with_logits(
            labels=y_, logits=y), name="cross_entropy")
    train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

    epochs = 1000
    show_count = epochs // 10

    sess = tf.InteractiveSession()
    tf.global_variables_initializer().run()

    [op.outputs for op in tf.get_default_graph().get_operations()]

    # see W is zero now
    # W_value = sess.run(W)
    # np.unique(W_value)
    
    # Train
    for index in range(epochs):
        batch_xs, batch_ys = mnist.train.next_batch(100)
        sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
        if index % show_count == 0 or index + 1 == epochs:
            print("handle {}%...".format((index+1) * 100 // epochs))
            # Test trained model
            correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
            accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
            acc_value = sess.run(accuracy, feed_dict={
                    x: mnist.test.images, y_: mnist.test.labels})
            print("accuracy:{}".format(acc_value))

    #Create a saver object which will save all the variables
    saver = tf.train.Saver()
    #Now, save the graph
    saver.save(sess, 'mnist_softmax', global_step=1000)

    
def restore_and_test():
    data_dir = "./data"
    mnist = input_data.read_data_sets(data_dir, one_hot=True)

    sess=tf.Session()    
    #First let's load meta graph and restore weights
    saver = tf.train.import_meta_graph('mnist_softmax-1000.meta')
    saver.restore(sess,tf.train.latest_checkpoint('./'))

    [op.outputs for op in tf.get_default_graph().get_operations()]

    graph = tf.get_default_graph()
    x = graph.get_tensor_by_name("x:0")
    y = graph.get_tensor_by_name("y/add:0")
    y_ = graph.get_tensor_by_name("y_:0")

    W = graph.get_tensor_by_name("W:0")
    W_value = sess.run(W)
    # you can see the values of W
    # the most import value in neuron network
    # the main difference with simple example.
    np.unique(W_value,return_counts=True)
    # 
    # (array([-0.66475219, -0.66456056, -0.65921789, ...,  0.63828367,
    #          0.69256693,  0.72933155], dtype=float32),
    #  array([1, 1, 1, ..., 1, 1, 1]))


    # Test trained model
    correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    print(sess.run(accuracy, feed_dict={x: mnist.test.images,
                                      y_: mnist.test.labels}))

main()