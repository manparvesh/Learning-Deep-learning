# Enter an interactive TensorFlow Session.
import tensorflow as tf
sess = tf.InteractiveSession()

x = tf.Variable([1.0, 2.0])
a = tf.constant([3.0, 3.0])

# Initialize 'x' because it is a variable and before running we need to make it constant
x.initializer.run()

# Now we can subtract
sub = tf.sub(x, a)
print sub.eval()
# ==> [-2. -1.]

add = tf.add(x, a)
print add.eval()
# ==> [ 4. 5.]       <- see there is a space for sign, too!

# Close the Session when we're done.
sess.close()
