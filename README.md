# Learning-Deep-learning

## Notes
 * TensorFlow is a programming system in which you represent computations as graphs. Nodes in the graph are called **ops** (short for operations). An op takes zero or more Tensors, performs some computation, and produces zero or more Tensors. A **Tensor** is a typed multi-dimensional array. For example, you can represent a mini-batch of images as a 4-D array of floating point numbers with dimensions **[batch, height, width, channels]**.
 * A TensorFlow graph is a description of computations. To compute anything, a graph must be launched in a **Session**. A **Session** places the graph ops onto **Devices**, such as CPUs or GPUs, and provides methods to execute them. These methods return tensors produced by ops as [numpy](www.numpy.org) **ndarray** objects in Python, and as **tensorflow::Tensor** instances in C and C++.
 * 
