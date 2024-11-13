import math
from math import factorial


def cal(a,b):
    return (a+b)

print("cal of two number is :",cal(10,20))

# Example 4 : function does not argument not return any value
def func(i):
    i=10
print(func(10))
# output : None

# example : we can declare the function by two types return statment or print ()
# function take arguments but no return value
def func1(a,b):
    print(a+b)
func1(10,20)


# example: function does not take argument but return some value.
def func2(a,b):
    return (a+b)
print(func2(10,20))

# example : function take the argument and also take the return value

# Add two numbers using functions:
# def func_3(a,b):
#     return (a+b)
# a=int(input("Enter the first number :"))
# b=int(input("Enter the second number :"))
# print(func_3(a,b))


# find factorial of number
# def func_4(a):
#     return math.factorial(a)
# result = func_4(4)
# print(result)

# logic concept
def func_5(a):
    return(a)
a=int(input("Enter the number value :"))
for i in range(a):
    result=factorial(i+1)
print(result)


# example
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

a = int(input("Enter the number value: "))

for i in range(a):
    result = factorial(i + 1)
    print(f"Factorial of {i + 1} is {result}")
# ---------------------------------------------------------------------





