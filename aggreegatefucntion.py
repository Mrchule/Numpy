import numpy as np

arr=np.array([[1,20,3,4,50],[9,8,7,6,5]])
arr1=np.array([[52,3,3,10,12],[4,53,34,22,77]])
a=np.arange(1,20,3)
b=np.arange(2,22,3)
print(a,b)
arr3=np.array([a,b])

print("addition of the two array is: ",arr3)

print("row wise max value =",arr.max(axis=1))
print("column wise max value =",arr.max(axis=0))
print("row wise min  value =",arr.min(axis=1))
print(" coloumn wise min value =",arr.min(axis=0))