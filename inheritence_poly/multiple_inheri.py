# need to crate of object class bases
class A:
    def func(self):
        print("class a method ")
class B(A):
    def func1(self):
        print("class b method")
class C(B):
    def func2(self):
        print("class c method")

obj=A()
obj1=B()
obj2=C()
obj.func()
obj1.func1()
obj2.func2()

# note: if there are multiple constructor like a,b,c so it's depend on the object basis e.g. if I create a object of b class than it call
# constructor of B class.


