# overriding : method haveing same name but diff parameter

class Student:
    def student(self,age,name):
        self.age=age
        self.name=name
        print(f"method having same name but different parameter : student :{age},student:{name}")

class lacture(Student):
    def speed(self,height,weight):
        self.height=height
        self.weight=weight
        print(f"overriding :height:{height},weight:{weight}")

        print("\n start execution of lacture")

        super().student(21,'akshay')

obj=lacture()
obj.speed(21,60)

