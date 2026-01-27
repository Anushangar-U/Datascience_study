#Create an $8 \times 8$ matrix that looks like a checkerboard of 0s and 1s.
import numpy as np

z = np.zeros((8,8), dtype=int)
z[1::2,::2] = 1
print(z)
print()
z[::2,1::2] = 1
print(z)
