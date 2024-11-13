# types of method :
# instance method : we can call them using/through object only
# static method : we can it directly


class MyClass:
    def m1(self):
        print("this is instance method")
    @staticmethod
    def m2(self):
        print("this is static method",self)


obj1=MyClass()
obj1.m1()

# obj2=MyClass()
# obj2.m2(1)
MyClass.m2(1)
