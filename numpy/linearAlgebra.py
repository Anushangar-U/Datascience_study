import numpy as np

a = np.ones((2,3))
b = np.full((3,2),2)

#matrix multiplication
result = np.matmul(a,b)
print(result)

c = np.identity(3)
print(c)

#find determinant
det = np.linalg.det(c)
print(det)

#inverse of matrix
inv = np.linalg.inv(c)
print(inv)


