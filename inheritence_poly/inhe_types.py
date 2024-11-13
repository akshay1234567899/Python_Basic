class A:
    def func(self):
        print("constructor of A")
    @staticmethod
    def m1(self):
        print("constructor of class A")

class B(A):
    def func1(self):
        print("constructor of B")
        super().__init__()
    def m3(self):
        print("constructor of class B")

obj2=B()
obj2.func1()
obj2.m3()
A.m1(1)
obj=A()
obj.func()


