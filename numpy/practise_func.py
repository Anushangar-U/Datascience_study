import numpy as np

a = np.array([1,2,3], dtype="32")
print(a)

b = np.array([2,4,6,8,9],[3,4,5,6])
print(b)

#getting demension
print(f"dimension of a : {a.ndim}")

#getting shape
print(f"shap of b : {b.shape}")

#getting type
print(f"a type : {a.dtype}")
 
#getting size
print(f"a itemsize : {a.itemsize}")

#getting total size
print(f"a size : {a.size}") 

#get a specific column[r,c]
b[1,3]

#get a specific row/cloumn [r/c,:]
b[0,:]

#specific slice or part [[r],starting index[c]:endindex[c]:stepindex]
b[0,0:4:2]

#changing data
b[1,3] = 20
print(b)

#changing all row/column
b[:,2] = 16
print(b)
b[:,1] = [9,0]
print(b)

