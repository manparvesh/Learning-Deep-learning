import tensorflow as tf

in1 = tf.placeholder(tf.float32)
in2 = tf.placeholder(tf.float32)
output = tf.mul(in1, in2)

with tf.Session() as sess:
    # set values to in1 and in2 by setting the feed_dict
    print(sess.run([output], feed_dict={in1:[7.], in2:[2.]}))
