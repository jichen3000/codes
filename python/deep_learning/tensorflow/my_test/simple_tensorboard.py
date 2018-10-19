import tensorflow as tf
import numpy
from minitest import *

def main():
    with tf.name_scope("variables") as scope:
        a = tf.constant(5, name='alpha')
        W = tf.Variable(tf.random_uniform([1, 2], -1.0, 1.0), name='weights')
        b = tf.Variable(tf.zeros([1]), name='biases')
        c =tf.reduce_mean(W)
        tf.summary.scalar("c",c)
        with tf.Session() as sess:
            merged = tf.summary.merge_all()
            train_writer = tf.summary.FileWriter("train", sess.graph)
            sess.run(tf.global_variables_initializer())
            # r_a, r_W, r_b = sess.run([a,W,b])
            r_summary, r_a, r_W, r_b, _ = sess.run([merged,a,W,b,c])
            train_writer.add_summary(r_summary,1)
            train_writer.close()
    # result.pp()
    r_a.pp()
    
main()
print("OK")