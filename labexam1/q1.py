import numpy as np

x = np.array([1,2,3,4,5])

y = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

z = np.array([[[1,2,3],[4,5,6]],
              [[7,8,9],[10,11,12]]])

print("Elements of 1D array: (indexing)",x[3])
print("Elements of 1D array: (slicing)",x[:3])

print("Elements of 2D array: (indexing)",y[1][0])
print("Elements of 2D array: (slicing)",y[0:2,:])

print("Elements of 3D array: (indexing)",z[1][0][1])
print("Elements of 3D array: (slicing)",z[0:2,:,:])
