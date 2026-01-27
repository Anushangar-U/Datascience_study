#Create an array of 10 random integers between 1 and 100.
#Replace every number greater than 50 with the value 999.

import numpy as np
A = np.random.randint(1,101,size=10)

mask = (A > 50)
A[mask] = 999
print(A)