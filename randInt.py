import numpy as np

arr=np.random.rand(7) # this rand function return random number between 0 to 1
print("random numbe from 0-1 ", arr)
randnum=np.random.randint(4)# this function return a single random integer value between 0 to 4 
print("a single random integer value",randnum)
arr1=np.random.randn(5)
print("random number close to zero",arr1) # this function return an array of random values closed to zero , it may be negative and + ve values
arr2=np.round(np.random.ranf(5)*100)

print("the random float +ve number ",arr2) # it return only +ve random float numbers between 0-1
print("this is integer type array :",arr2.astype(int))# astype function is used to change the type of the array 
print("this is float type ",arr2.astype(float)) 


arr3=np.random.randint(10,100,20) #this function return only interger in a given range 
arr4=np.random.randint(0,10,5)
print("the random array is :",arr3)
print("the random array is :",arr4)

arr5=np.empty(5)
print("Is this an empty array ",arr5)