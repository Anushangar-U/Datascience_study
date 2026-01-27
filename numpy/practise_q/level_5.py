#The Goal:Create a 1D array A = [1, 2, 3].Use np.newaxis to calculate a Subtraction Table.The result should be a $3 \times 3$ matrix where the value at [i, j] is A[i] - A[j].
import numpy as np

A = np.array([1,2,3])
diff = A[:,np.newaxis] - A[np.newaxis,:]
print(diff)
