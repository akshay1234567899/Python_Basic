from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def m1(self):
        None
    @abstractmethod
    def m2(self):
        None

class B(A):
    def m1(self):
        print("test")

class C(A):

    def m2(self):
        print("test -c ")

    def m1(self):
        print("test-a")


obj=C()
obj.m2()
obj.m1()