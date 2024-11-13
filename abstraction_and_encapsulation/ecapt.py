class Branch:
    def __init__(self,name,code):
        self.__name=name
        self.__code=code

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,new_name):
        self.__name=new_name

    @property
    def code(self):
        return self.__code


    @code.setter
    def code(self,new_code):
        if new_code>=100000:
            self.__code = new_code
        else:
            print("Enter a 6 digit number")

obj=Branch('ICICI',178956)
print("Bank Name :",obj.name)
print("Bank Code :",obj.code)

obj.name="SBI"
obj.code=900293

print("Updated Bank Name :",obj.name)
print("Updated Bank Code :",obj.code)
obj.code=90029