from abc import ABC, abstractmethod

# note: abstract method bydefault, when call abstract method in anothe class

class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

class Sparrow(Animal):
    def eat(self):
        print("absract from concreate class ")

class Cow(Animal):
    def eat(self):
        print("abstact from concreate")

obj=Cow()
obj.eat()

