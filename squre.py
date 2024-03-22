# a=5 
#a=int(input("enter a number "))
#print("square of the number is =",a**2)
# a=5
# b=10
# print(" max number is ",max(a,b))
import numpy as np 

# a=np.array([30,45,60,90])
# print("max  :",a.max())
# print("sum  :",a.sum())
# print("min  :",np.min(a))
# print("avg  :",np.average(a))
# print("sine value",np.sin(np.floor(a)))
# print("sine value",np.cos(a))


# a=[]
# for i in range(1,50):
#     l=int(input("enter : "))
#     a.append(l)
# print(a)
    
var1=np.array([1,2,3,4])
var2=np.array([1,2,3,4])

var3=var1+var2
# print(var3)
var=np.array([[1,2,3,4,5],[5,6,7,8,9],[0,7,8,9,6]])
vaar=np.array([[[1,2,3,4,5],[5,6,7,8,9],[0,7,8,9,6]]])
print(vaar.ndim)
# print("addition of two array",var/vaar)
# print(var)
print(vaar)
varr=var.copy()
print("size of the array",varr)

# for i in var:
#     for j in i:
#         print(j)
#     print("------")

var4=np.array([[[1,2,3],[2,3,4],[4,5,6],[5,6,7]]])

print(var4.ndim)
print("------------")

for i in var4:
    for j in i:
        for k in j:
            print(k)
        print("--+--")
    print("-----++-----")        