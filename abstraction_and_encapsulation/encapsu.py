class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if new_age > 0:
            self.__age = new_age  # Correctly assign to the private attribute
        else:
            print("Age cannot be negative")

s = Student('Akshay', 20)

print("Name:", s.name)  # Output: Name: Akshay
print("Age:", s.age)    # Output: Age: 20

s.name = 'Ravi'
s.age = 25
print("Updated Name:", s.name)  # Output: Updated Name: Ravi
print("Updated Age:", s.age)    # Output: Updated Age: 25

s.age = -5  # Output: Age cannot be negative
