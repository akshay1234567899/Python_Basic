class employee:
    def __init__(self,eid,ename,esal):
        self.eid=eid
        self.ename=ename
        self.esal=esal

    def display(self):
        print(self.eid,self.ename,self.esal)

# obj1=employee(101,'akshay',10000)
# obj1.display()