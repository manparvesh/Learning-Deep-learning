import tensorflow as tf

# 2X1 matrix
mat1 = tf.constant([[3., 3.]])

# 1X2 matrix
mat2 = tf.constant([[2.], [2.]])

# multiply both of 'em
product = tf.matmul(mat1, mat2)

# print product
# ^outputs a tensor object in the form: Tensor("MatMul:0", shape=(1, 1), dtype=float32)
# i guess that 0 is because the multiplication has not been run yet

# launching graph in a session
# create new session
sess = tf.Session()

# running the session with input parameter as the product, and the session would run 3 ops in the graph. 
# the 2 constant matrices, and the product matrix
result = sess.run(product)
# result will be a numpy 'ndarray' object

print (result)
# should be [[ 12.]]

#close the session now
sess.close()
