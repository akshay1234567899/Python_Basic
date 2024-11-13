class A:
    a, b = 10, 20
    def m1(self):

        print(self.a+self.b)
class B(A):
    c,d=100,200
    def m2(self):
        print(self.c+self.d)

obj=B()
obj.m1()
obj.m2()