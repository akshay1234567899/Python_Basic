# variable :
# local :
# global :

# instance variable/class variables  : if we declare the varilables under the class
class MYClass:
    a,b=10,20
    def add(self):
        # print(a,b) # invalid
        print(self.a+self.b)

add1=MYClass()
add1.add()


# example :
i,j=15,25
class MYFirst:
    a,b=10,20    # instance variable
    def add(self,x,y):  # local variable
        print(x,y)
        print(self.a+self.b) # instance varialbe
        print(i,j)    # gloabl variable
obj=MYFirst()
obj.add(1,23)