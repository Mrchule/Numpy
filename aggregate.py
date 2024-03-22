import numpy as  np

arr=np.array([[20,30,40,50],[111,12,13,14]])
# arr1=np.array([[2,3.4,40.5,20],[11,102,123,14]])
# print(np.min(arr))
# print("the given array",arr)
# print("dimenssion of the array ",arr.ndim)
print(arr)
print("the min value of the array is ", np.min(arr)) # this return a single value which is minimum
print("this is the argmax of the given array",np.argmin(arr,axis=1)) # this function return the index of smallest number in the array 

print("cols wise min value af the array i.e axis 0",np.min(arr,axis=0)) # this function return a minimum value of the array coloum wise .. axis 0 means the column wise
print(" min value af the array in the axis 1 i.e in the rows",np.min(arr,axis=1)) #this function  return a minimum value  in the array (row wise)

print("the cummulative sum of the array is ", np.cumsum(arr,axis=0))#let arr [1,2,3,4,5] so here output will be [1,1+2,1+2+3,1+2+3+4,1+2+3+4+5]

print("mean of the element that are present in the array is :",np.mean(arr,axis=1))
 # so this function return the mean value  of the array or we can say average
print("average of the element that are present in the array is :",np.average(arr))

print("median of the element that are present in the array is :",np.median(arr))
 # so this function return the meddian value  of the array.
print("corelation cofficent of the array is :",np.corrcoef(arr)) # this function return  corelation cofficent of the array 
print("standard daviation of the array is :",np.std(arr)) # this function return the standard daviation of the elements of the array 
print("the sum of the element array wise ",np.sum(arr))
print("the sum of the element array wise ",arr.sum())

