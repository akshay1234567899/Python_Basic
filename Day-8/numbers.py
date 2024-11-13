# a+bj
# complex number a -- real number, b --- imag
import math
from math import factorial
from unicodedata import decimal

a=20+4j
print(type(a))
print(a.real)
print(a.imag)
print(a.__complex__())

a1=0.4+3j
print(a1.__complex__())

# Type of conversion in complex number
#  implicit ,
#  explicit

num1=int(5)
print(num1)

# implecit
a=0.10
b=20.12
c=a+b
print(c)
print(round(c,2))
print(f"{c:.2f}")
# print("{:.2f}",format(c))
# ______________________________________________
# absolute value in pythone
a=10.09
print(abs(a))

b=-4
print(abs(b))

# ________________________________________________________
# power in numbers
print(pow(2,3))

# round off value
print(round(45.32224,2))
# print max and min
print(min(3,6,3,12,67,32))
print(max(5,20,42,49))
print(max(21.32,32.84))
# -------------------------------------------------------------

# Return tuple containing
print(divmod(90,3))
# print oct,hexa, octal number
print(oct(20))
print(hex(89))
print(oct(89))
print(bin(84))

# -----------------------------------------------------------
# type method : to print data type of number
a=49
print(type(a))

# ________________________-----------------------------------------
#  isinstance : to check the object is instance of a perticular class or object
print(isinstance(10.3,float))
print(isinstance(2,int))
# _____________________________________________________________________________
# factorial of number
num=8
print(math.factorial(num))
fac=math.factorial(9)
print(f"factorial of number {num} is :{fac}")
# --------------------------------------------------------------------------
# Collection : set of data

