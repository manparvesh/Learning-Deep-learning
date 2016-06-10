import tensorflow as tf

# new variable to count, initial value = 0
state = tf.Variable(0, name="counter")

# operation (op) to add to the counter
one = tf.constant(1)
new_val = tf.add(one, state) #either way works out?

# set new value
update = tf.assign(state, new_val)

# all variables need to be initialized before use. adding an op for the same
init_op = tf.initialize_all_variables()

#launching graph
with tf.Session() as sess:
    # init operation first
    sess.run(init_op)
    
    # initial value of state (0)
    print sess.run(state)
    
    # update and print values (from 1 to 10)
    for _ in xrange(10):
        sess.run(update)
        print sess.run(state)
