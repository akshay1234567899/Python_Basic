# class A:
#     __a=10
#     def display(self):
#         print("print private method")
#         obj.__a
#
# obj=A()
# obj.display()
# =========================================================================================
class myclass:
    __empid=101   # private variable (can not change the value)
    def getempid(self,eid):
        self.__empid=eid

    def dispeid(self):
        print(self.__empid)

obj=myclass()
obj.dispeid()
obj.getempid(20)

