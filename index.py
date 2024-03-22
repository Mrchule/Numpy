import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])

rows = np.array([0, 1])
cols = np.array([1, 2])
print(arr[rows, cols]) 
print(arr[[0,1],[1,2]])
print(arr)
# print(arr[1,2])

