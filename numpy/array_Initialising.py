import numpy as np

#all matrix to zero
a = np.zeros(5)
print(a)

#all ones matrix 
a = np.ones(6)
print(a)

#any number
a = np.full((2,2),9)
print(a)

#random decimal
a = np.random.rand(4,2)
print(a)

#randoom int
a = np.random.randint(4,2,size=(3,3))
print(a)

#the identity matriz
a = np.identity
print(a)

#repeat an array
arr = np.array([1,2,3])
r1 = np.repeat(arr,3,axis = 0)
print(r1)