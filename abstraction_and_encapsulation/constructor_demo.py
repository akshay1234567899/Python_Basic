# how to create and access constructor in abstract class

from abc import ABC, abstractmethod
# class cal(ABC):
#     def __init__(self,value):
#         self.value= value
#
#     @abstractmethod
#     def add(self):
#         pass
#
#     def sub(self):
#         print(self.value-100)
#
# class result(cal):
#
#     def add(self):
#         print(self.value + 100)
#
# obj=result(10)
# obj.add()

# class >shap(abstract[area,perimeter])
# class rect(shape)---area, perimeter,weidth, height

class shap(ABC):
    def __init__(self,weidth,height):
        self.weidth=weidth
        self.height=height

    @abstractmethod
    def area(self):
        None
    def perameter(self):
        None

class rect(shap):
    def area(self):
        print("area of circle :",self.weidth*self.height)

    def perameter(self):
        result= self.weidth+self.height
        print("perameter of circle :",2*result)


obj=rect(10,20)
obj.area()
obj.perameter()