#input -- build in function in python library
from tokenize import String

num1=input("enter first number ")
num2=input("enter second number ")
add=num1+num2
print(add)

#type conversion : converting the data from one type to another type

#String---interger
#implicit-- automatically perform by the interpreter
# explicit -- instruction programmer need to give int (), float(), boolean()

a=20
print(type(a))

#------------------------------------
#explicit example :-

num1=input("enter first number ")
num2=input("enter second number ")
print(int(num1))
print(int(num2))
add=num1+num2
print("additional of two number=",add)

#------------------------------------------------------------------
print(input(num1+num2))
