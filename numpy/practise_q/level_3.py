# Create two random arrays, A and B, both of shape $(10, 2)$. These represent 10 coordinates $(x, y)$.
# Calculate the Euclidean distance between each pair ($A[0]$ to $B[0]$, etc.) in a single line of code.

import numpy as np

A = np.random.randint(0,10,size = (10,2))
B = np.random.randint(0,10,size = (10,2))

D = np.sqrt(np.sum((A-B)**2,axis= 1))