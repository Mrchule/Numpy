import numpy as np

arr=np.array([[5,6,7],[1,2,3]])

for i in arr:
    for j in i:
        print(j)

print("each element of the array by using nditer methode ")# nditr means n-dimenssion itteration

for i in np.nditer(arr):
    print(i)

print("each element and indexing of each element") 

for i,d in np.ndenumerate(arr):
    print(i,d)
print("the index and element")
for i,j in np.ndindex(arr):
    print(i)