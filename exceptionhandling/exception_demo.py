# exception : is an event which cause the progream termination.
from doctest import Example

# systex error : generated always by the inteprator
# logical error : logical error by dev like perform a+b but performed by mistake a-b
# run time error : which occur at the run time or execution time.

# try
# except
# else
# finally

# example:
print("this is the staring of the program")
print("this is the staring of the program")
print("this is the staring of the program")
print("this is the staring of the program")
print("this is the staring of the program")
print(10/2)

# print(10/0)  ------ZeroDivisionError: division by zero (run time error)
# to avoid termination we need to handle the exception. to handle the exception we have try except else and finally block are used.

print("this is the ending of the program")
print("this is the ending of the program")
print("this is the ending of the program")

# try : code that might couse the exception
# except/except someExceptionName : code to handle the exception

# else : code to execute if no exception occured
# finally : code that will run no matter what & it is maindatory to use with try except block.


# example-2 :

print("this is the staring of the program")
print("this is the staring of the program")
print("this is the staring of the program")
print("this is the staring of the program")
print("this is the staring of the program")

try:
    print(10/0)
except:
    print("The exception occure in the code :)")

print("this is the ending of the program")
print("this is the ending of the program")
print("this is the ending of the program")

# exapmle-3:
print("this is the staring of the program")
print("this is the staring of the program")
print("this is the staring of the program")
print("this is the staring of the program")
print("this is the staring of the program")

try:
    print(10/0)
except Exception as e:
    print(e)

print("this is the ending of the program")
print("this is the ending of the program")
print("this is the ending of the program")


# build in exception:
# Exception, AttributeError,EOFError,IndexError,KeyError,KeyboardInterrupt,NameError(a=10,del a, print(a)),StopIteration,TypeError(pass string value instead of int),ValueError and ZeroDivisionError


# Example -4 :Multiple except block

num1,num2=10,2
try:
    result=num1/num2
except ZeroDivisionError as e:
    print(e)
except ZeroDivisionError:
    print("Thrown ZeroDivisionError exception")
except FileNotFoundError:
    print("file not found exception")
except SyntaxError:
    print("Syntax Error occured")
#     parent class exception handling
except Exception as e:
    print(e)
#     print all the time if exception occure or not
finally:
    print("excute always")


# raising our own exception ----------------------------------------------
def enterage(num):
    if num<0:
        raise ValueError("only integers are allowed")
    if num%2==0:
        print("even")
    else:
        print("odd")
num=-6
# try:
#     enterage(num)
# except Exception as e:
#     print(e)

try:
    enterage(num)
except ValueError as e:
    print(e)

print('program terminated')


# User define exception : which is creating by the programmer.
# syntax: class customError
class customError(Exception):
    pass
try:
    raise customError ("this is custom error message")
except customError as e:
    print("value not passed")

# Example :
class NegativeNumberError(Exception):
    pass
try:
    raise NegativeNumberError (" -- ")
except NegativeNumberError as e:
    print(" ----- ")