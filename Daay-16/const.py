from copyreg import constructor

# constructor name is fixed def __init __(self)
# constructor will be called automatically at the time of object creation.
# constructor will not return any value

class MyClass:
    def __init__(self):
        print("consturctor here")

    def m1(self):
        print("I am method of the class")

objec=MyClass()
objec.m1()  # method call explicitely by using object

