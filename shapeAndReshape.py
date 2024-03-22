import numpy as np

arr=np.array([1,2,3,4,5,6,7,8,9])
print(arr.ndim)
print(arr.shape)
# print(arr)
arr=arr.reshape(3,3)
# print(arr)
print(arr.ndim)

arr2=np.array([1,2,3,4,5,6,7,8])

print("shape of arr is :",arr2.shape ,"  dimenssion :",arr.ndim)

arr2=arr2.reshape(2,4,1,1)
print("shape of arr is :",arr2.shape ,"  dimenssion :",arr.ndim)
print(arr2)

arr3=np.random.rand(3,3,4)
arr3=np.round(arr3*100)
print("the random array is ",np.round(arr3))
arr4=arr3.reshape(2,9,2)
print(arr4)

print()

arr5=np.arange(1,100,3)
print("the length of the array is ",len(arr5))
print(arr5.reshape(3,11))
print(arr5.reshape(11,3))
arr6=np.linspace(2,30,5 , dtype=int)
print(arr6)
arr7=np.array([[2]])
print(arr7.shape)