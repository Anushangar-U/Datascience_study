import numpy as np

data = np.genfromtxt('data.txt', delimiter=',')
data = data.astype('int32')
print(data)

#boolean masking and advance indexing
mask = data > 50
print(f"Mask of values greater than 50:\n{mask}")

#you can index with a list in numpy
a = np.array([10,20,30,40,50])
accessed_elements = a[[1,3,4]]
print(f"Accessed elements at indices 1, 3, 4: {accessed_elements}")


