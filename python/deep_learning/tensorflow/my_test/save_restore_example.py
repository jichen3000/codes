# https://stackoverflow.com/questions/33759623/tensorflow-how-to-save-restore-a-model

import tensorflow as tf

def train_and_save():
    #Prepare to feed input, i.e. feed_dict and placeholders
    w1 = tf.placeholder("float", name="w1")
    w2 = tf.placeholder("float", name="w2")
    b1= tf.Variable(2.0,name="bias")
    feed_dict ={w1:4,w2:8}

    #Define a test operation that we will restore
    w3 = tf.add(w1,w2)
    w4 = tf.multiply(w3,b1,name="op_to_restore")
    sess = tf.Session()
    sess.run(tf.global_variables_initializer())


    #Run the operation by feeding input
    w4_value = sess.run(w4,feed_dict)
    print(w4_value)
    #Prints 24 which is sum of (w1+w2)*b1 

    #Create a saver object which will save all the variables
    saver = tf.train.Saver()
    #Now, save the graph
    saver.save(sess, 'my_test_model',global_step=1000)

    print("train_and_save end!")

def restore_and_run():
    sess=tf.Session()    
    #First let's load meta graph and restore weights
    saver = tf.train.import_meta_graph('my_test_model-1000.meta')
    saver.restore(sess,tf.train.latest_checkpoint('./'))


    # Access saved Variables directly
    b1_value = sess.run('bias:0')
    print(b1_value)
    # This will print 2, which is the value of bias that we saved

    # cannot directly get the w4, since it depends on w1 and w2
    # w1 and w2 need to be input
    #w4_value = sess.run('op_to_restore:0')


    # Now, let's access and create placeholders variables and
    # create feed-dict to feed new data
    graph = tf.get_default_graph()
    w1 = graph.get_tensor_by_name("w1:0")
    w2 = graph.get_tensor_by_name("w2:0")
    feed_dict ={w1:13.0,w2:17.0}

    #Now, access the op that you want to run. 
    w4 = graph.get_tensor_by_name("op_to_restore:0")

    w4_value = sess.run(w4,feed_dict)
    print(w4_value)
    #This will print 60 which is calculated 

    # see all operator tensor name
    graph.get_operations()
    [op.outputs for op in tf.get_default_graph().get_operations()]
