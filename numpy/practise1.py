import numpy as np

a = np.ones((5,5))
b = np.zeros((3,3))

a[1:4,1:4] = b
a[2,2] = 9

print(a)