import numpy as np 

a=np.array([1,2,3,4,5,6,7])

print(a[3::]) 
 # it will skip the number of element that pass after double collon and print rest  of the element  [4,5,6,7]
print(a[::3])
 #it will start printing element  start from index 0 and skip 3 element including first element

arr=np.array([[10,20,30,40,50],[11,12,13,14]])

rows=np.array([1,2])
cols=np.array([1,2])

print(arr[cols,rows])
