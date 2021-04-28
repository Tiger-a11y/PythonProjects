# from numpy import *
# arr = array('i',[])
# n = int(input("enter the lenght of array :"))
#
# for i in range(n):
#     x = int(input("enter the value :"))
#     arr.append(x)
# print(arr)
#
# val = int(input("Enter the value you wanna search :"))
# k = 0
# for e in arr:
#     if e == val:
#         print(k)
#         break
#     k = k+1
# print(arr.index(val))
from numpy import *

#
# Arr = array([1,2,3,4,5,6])
# print(Arr.dtype)
# print(Arr)

# !! Matricess Array !!  #

# arr1 = array([[1,2,3,5,7,8],
#              [4,5,6,4,2,3,]]
#              )
# arr2 = arr1.flatten()       # .flatten - to convert 2 dim to 1 dim
#
# arr3 = arr2.reshape(2,2,3)           #
#
# print(arr3)            # .dtype, .nim, .shape, .size,


m1 = matrix('1 2 3 ; 5 6 9 ; 4 5 6 ')
m2 = matrix('2 3 1 ; 6 5 8 ; 7 5 3')
m3 = m1*m2
print(m3)