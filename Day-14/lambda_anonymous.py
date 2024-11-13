# lambga or anonymous func : a func which has no name.
# A lambda func can take any number of arguments, but it has only one expression
# lambda func generally used with filter(),map(),sorted() functions
from audioop import reverse
from functools import reduce

# syntax : lambda arguments:expression
# Example
x=lambda a:a+10
print(x(5))

# =================================================
# example
x=lambda a,b:a*b
print(x(4,5))

# example

list1=[11,23,43,53,67,39,63]
# def even(x):
#     return x%2==0
# evennumber=list(filter(even,list))
# print(evennumber)

# =======================================================
number=[10,11,12,13,14,15,16,17,18]
result=list(filter(lambda x:x%2==0,number))
print(result)
# =========================================================
# sorting
list_1=['palamput','una','shimla','rampur','bilaspur']
result=sorted(list_1,key=lambda x:(len(x)))
print(result)

# ==================================================================
# reverse city
City=['palamput','una','shimla','rampur','bilaspur']
def length(city):
    return len(city)
sort=sorted(City,key=length,reverse=True)
print(sort)
# _________________________________________________________
num=[1,2,3,4,5,6]
result=list(map(lambda x:x**2,num))
print(result)
# ========================================================
# limitation of lambda : not suitable for complext problem
# less readable,
def square(num):
    return num
result=list(map(lambda x:x**2,num))
print(result)

# ================================================================
# reduce : pick two numbers from the list , from functools import reduce
result=reduce(lambda x,y:x+y,[1,2,3,4])
print(result)

# ====================================================================
# Sorted : sorted(iterable, key=name,reverse=false)
a=sorted([20,10.4,5,18,32,1])
print(a)
# ======================================================================
# zip : zip the two iterator  (in the form of tuple format)
a=[10,20,30]
b=[40,50,60]
c=a+b