# example
class Myclass:
    def __init__(self):
        print("name")
    def display(self,stuname):
        print(stuname)

obj=Myclass()
obj.display("name")

# how we passing parameter in consturctor
class display:
    name="scott"  # instance variable
    def __init__(self,name):
        print(name)
        print(self.name)
obj1=display("akshay")


class emp:
    def __init__(self,eid,ename,esalary):
        self.eid=eid
        self.ename=ename
        self.esalary=esalary
        print(self.eid,self.ename,self.esalary)  #self (instance keyword) to print the value
obj2=emp(101,'akshay',10000)






