# example : two parent and one child
class A:
    def func(self):
        print("this is method from class A")

class B:
    def func(self):
        print("this is method of class B")

class C(A,B):
    a=10
    def func_1(self):
        print("instance variable",self.a)
obj=C()
obj.func()
obj.func_1()