# variable
# *args ----- positional variable length arguments
# **kwargs -------- kwyword variable length arguments
# allows a func to accept any no of positional arguments, which will be passed as a tuple to the function.
from doctest import Example

# sum(10,20)
# sum(10,20,30)
# sum(10,20,30,40)
# --------------------------------------------------------------------------------------------
# stud(name="",age="",rollno="")
# Example :
def greet(*args):
    print("hello", {args})

greet("akshay")
# value pass in the form of tuple
greet("akshay","dhiman","tuple")


# ----------------------------------------------------------------------------------
# example kwargs
# allow a func to accept any numbers of keyword arguments passed as a key value pair i.e. dictionary
def stud_info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} :{value}")
stud_info(name="bob",id=102,course="py")

# -------------------------------------------------------------------------------------------
# combination of args and kwargs
def display_info(*args,**kwargs):
    print("positional arguments",args)
    print("keywords arguments",kwargs)
display_info(1, 2, 3, name="ram", id=1, city="PB")

# args is used to pass a variable number of positional argument as tuple
# kwargs is used to pass a variable number of keyword argument as distionary
# we can combine both in same function to acheive flexibility

# =============================================================================

# example 4:
def func(name,*args):
    print(args,name)
func("akshay","dhiman","bob",30)

# ============================================================================
def func1(name,*args,**kwargs):
    print((name,args,kwargs))
func1("ram",40,"kon")

# ==========================================================================
def func2(name,*args,**kwargs):
    print(name)
    for i in args:
        print(i)
        for i,j in kwargs.items():
            print(f"{i},{j}")
func2("akshay",2,25,name2="dhiman",age=30)



