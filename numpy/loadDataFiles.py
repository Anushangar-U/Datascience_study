import numpy as np

data = np.genfromtxt('data.txt', delimiter=',')
data = data.astype('int32')
print(data)

