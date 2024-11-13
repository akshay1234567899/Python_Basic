class MyClass:
    def __init__(self,eid,ename,esalary):
        self.eid=eid
        self.ename=ename
        self.esalary=esalary

# method-2
    def display(self,eid,ename,esalary):
        print(eid,ename,esalary)

obj=MyClass(101,'zyx',10222)
print(obj.esalary)  # method-1
obj.display(101,'zyx',10222)

# delete the element : we can delete the property of object or entire object
del obj.esalary
print(obj.esalary)
obj.display(101,'zyx',10222)

# delete the object
del obj