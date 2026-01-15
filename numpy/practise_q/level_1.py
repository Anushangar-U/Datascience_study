#Create a 1D array of 20 random integers between 1 and 50. Then, replace all even numbers in that array with the value -1.

import numpy as np

a = np.random.random_integers(1,50,size = 20)

print(f"original array : {a}")

a[a % 2 == 0] = -1

print(f"Modified array(-1) : {a}")