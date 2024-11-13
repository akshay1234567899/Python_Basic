# abstact method :  method that is declared which contain  no implementation.
# abstract classes : that contain one or more abstract method.
from abc import ABC, abstractmethod


class A(ABC):  # abstract base class
    @abstractmethod
    def m1(self):
        None

class B(A):  # abstract class
    def m1(self):
        print("Hello, I am concreate class now")
        # super().m1()

    @abstractmethod
    def m2(self):
        print("method two ")


class C(B):
    def m3(self):
        print("concreate class ")

    def m2(self):
        print("concreate from abstract class")

obj=C()
obj.m3()
obj.m2()
