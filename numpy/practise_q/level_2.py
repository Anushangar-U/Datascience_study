#Create a 5*5 matrix with values ranging from 1 to 25. Calculate the mean of each row and subtract that mean from every element in the corresponding row.

import numpy as np

A = np.random.randint(1,26, size = (5,5))

print(A)

A_row_mean = A.mean(axis = 1, keepdims=True)

result = A - A_row_mean

print(result)