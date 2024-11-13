# # using array function create a array
# from array import array
#
import numpy as np
#
# array1=np.arange(1,8)
# print(array1)
#
# reshape-- attribute
array1=np.arange(11,17).reshape(2,3)
print(array1)
# [[11 12 13]
#  [14 15 16]]
#
# # create an arrya with zero value
# arra_1=np.zeros(4).reshape(2,2)
# print(arra_1)
# # print(np.dtype(arra_1))
#
# #  output : floating data
# # [[0. 0.]
# #  [0. 0.]]
#
# # various attribute of numpy array
#
#
#
# list1=[10,20,30,40,50]
# array_01=np.array(list1)
# print(array_01)
#
# # ndim ----dimension of array
# print(array_01.ndim)
#
# # shap ----shape of array
# list_01=[[10,20,30],[40,50,60],[70,80,90]]
# array_1=np.array(list_01)
# print(array_1.shape)
#
# # size ----- total no of elements
# print(array_01.size)
#
# # dtype ----- type of an array
# print(array_1.dtype)
#
# list_02=["apple","mango","banana"]
# # list_03=['10.6','23.4']
# arr=np.array(list_02)
# print(arr.itemsize)
# # output :24
#
# # print(list_02.itemsize)
#
# # Manipulation and access the element  from an array
#
# array_03=np.array([10,20,30,40,50])
# print(array_03[-1])
# print(array_03[0])
#
# # 2-d array
# arr=np.array([10,20,30],[40,50,60],[70,80,90])
# print(arr[2])
# # 1st row and 2nd column
# print(arr[1][2])
# print(arr[:,1])
import numpy as np
from numpy.ma.core import subtract
from numpy.matrixlib.defmatrix import matrix

# slicing from arrays
array_sli=np.array([10,20,30,40,50,60])
print(array_sli[1:3])
print(array_sli[-1:-3:-1])


# Airthmatic operations on numpy arrays

# Addition: -----
x=np.array([[1,2],[3,4]])
y=np.array([[5,6],[7,8]])
z=x+y
print(x+y)


# subtract
print(x-y)

# multiple
print(x*y)

# matrix
print(x@y)

# Divison
print(x/y)
# floor division
print(y//x)
# module
print(y%x)
# transpose -- convert rows into column and vice versa
print(x.transpose())
print(y.transpose())


