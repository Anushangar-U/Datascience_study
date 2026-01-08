import numpy as np

bef = np.array([[1,2,3,4],[5,6,7,8]])
print(f"Original array:\n{bef}")

#reshaping array
aft = bef.reshape((4,2))
print(f"Reshaped array (4x2):\n{aft}") 

#vertical stacking
a = np.array([[1,2,3,4],[5,6,7,8]])
b = np.array([[9,10,11,12],[13,14,15,16]])
v_stack = np.vstack((a,b))
print(f"Vertically stacked array:\n{v_stack}")

#horizontal stacking
h_stack = np.hstack((a,b))
print(f"Horizontally stacked array:\n{h_stack}")