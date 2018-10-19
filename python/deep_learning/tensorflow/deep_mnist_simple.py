from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
import time

def simple_one(mnist):
  # inputs
  x = tf.placeholder(tf.float32, shape=[None, 784])
  y_ = tf.placeholder(tf.float32, shape=[None, 10])

  # 
  W = tf.Variable(tf.zeros([784,10]))
  b = tf.Variable(tf.zeros([10]))

  y = tf.nn.softmax(tf.matmul(x,W)+b)

  # cost function
  cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))

  # train
  # steepest gradient descent
  train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

  # sess = tf.InteractiveSession()
  with tf.Session() as sess:


    sess.run(tf.global_variables_initializer())



    for i in range(1000):
      # batch size is 50
      batch = mnist.train.next_batch(50)
      # train_step.run(feed_dict={x: batch[0], y_: batch[1]})
      sess.run(train_step, feed_dict={x: batch[0], y_: batch[1]})
      if i % 100 ==0:
        print("index",i)

    # evaluate
    correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))

    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

    accuracy_result = accuracy.eval(feed_dict={x: mnist.test.images, y_: mnist.test.labels})
    print("accuracy_result:",accuracy_result)

if __name__ == '__main__':
  mnist = input_data.read_data_sets('data', one_hot=True)
  simple_one(mnist)


