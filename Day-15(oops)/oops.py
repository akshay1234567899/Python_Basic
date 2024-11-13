# class and objects
# python : structed and oops
# class -- logical entity
# every class have some attribute and class include the method


# example :
# class emp{
# name()
# id()
# salary()
# leave()
# bonus()
# }

# object: physical entity
class MYName:
    def myfun(age,name):
        # pass means return a null value
        # pass
        print(age,name)
    # instance method
    def display(self,name):
        print('Hello Python',name)

obj1=MYName()
obj2=MYName()

obj1.myfun(20,"ram")
obj2.display("akshay")

obj2.myfun(20,"ram")
obj1.display("setup")

