import math
#from python_math import asin, acos
import numpy as np

a=6
b=1.2
#x=[3,4, asin(math.pi/8), acos(math.pi/10),a*b, math.sqrt(256)]
#y=[3.5,4.6, 1+asin(math.pi/8), 0.5+acos(math.pi/10),2+a*b, 0.36+math.sqrt(256)]
# to add two arrays we need numpy downloaded
#z=x+y
#print(x[0], x[2])
#***********************************************************************************
"""

i=0
d=0
z=[0]*6 #creating an empty array with all zeros of dimension 6
while i<len(x):
    d=d+x[i]
    z[i]=d
    i=i+1
    #print(d)
#print(z)
"""

#***********************Using numpy****************************************************

# array1=np.array([1,5,7,9,10])
# arr2=np.array([[9,0,3,4],[12, 10, 40, 50]])
# arr3=np.array([[5,15,20,35],[1,2,3,4]])
# arr4=np.array([[1,1,1,1],[0,1,2,5]])
# arr5=np.array([[5,15,20,35],[1,2,3,4],[2,6,7,9]])
# #print(arr5.ndim) # number of dimension is simply number of 'third bracket', indexing should be row and column 
# #print(arr5[2,1])
# arr6=np.array([1,2,3,4,5], ndmin=4)

#print(arr6[0,0,0,1]) # first index is the outer most one and the innermost one is the last index, 
# here 1 means the second element of the 4th dimension.
#***************************************************************************************
#print(arr6.dtype) #***************** This gives the data type of the array

#print(arr3[0:2,1:3]) 
# # '''**********first element means row and second element means column. First element is 0:2, 
# # means index 0 is row 1 and index 1 is row 2, and it excludes index 2.
# # Similarly second element means columns, index 1 means second column, 
# # index 2 gives 3rd column and index 3 is excluded ********'''

# print('x=', end='')
# x=int(input())
# print('y=',end='')
# y=int(input())
# print('z=',end='')
# z=float(input())

# print(x+y+z)
def func(a):
    result =3+a
    return result
    
def fpin(z,x):
    y=func(x)+z**2
    return y
    
def hun(p):
    f=func(2)+fpin(3,4)+p
    return f
    
print(func(2),fpin(3,4),hun(5))