# herachi-inheritence :
from email.policy import default

a,b=12,34
class A:
    def func(self):
        print("class A method")

    def __init__(self):
        print("constructor calling")

class B(A):
    def func1(self):
        print("class B method")
class c(A):
    def func2(self):
        print("class C method")
        print("Sum of global number are :",a+b)

obj=A()
obj1=B()
obj.func()
obj1.func1()
obj1.func()
obj2=c()
obj2.func2()
