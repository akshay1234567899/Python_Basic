# overloading : method having same name but different parameter.

# overloading : compile time polymorphism
#               run time polymorphism

class A:
    def sayhello(self,name=None):

      if name is not None:
        print("hello" + name)

      else:
        print("Hello")
obj=A()
obj.sayhello("akshay")




class calculation:
    def add(self,a=0,b=0,c=0):
        print(a+b+c)
cal=calculation()
cal.add(10,20)
