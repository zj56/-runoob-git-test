import numpy as np
from numpy import random
from numpy.core.fromnumeric import shape
t1 = np.arange(24)
# print(t1.shape)
# print(t1.reshape((2,3,4)))
print(t1.shape)
t5 = t1.reshape(3,8)
t6 = np.arange(100,124).reshape((8,3))
print(t5.dot(t6))


