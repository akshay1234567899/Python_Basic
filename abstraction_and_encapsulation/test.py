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
            self.__age = new_age  # Corrected this line
        else:
            print("Age cannot be negative")

# Creating an instance of Student
s = Student('Akshay', 20)

# Accessing properties
print("Name:", s.name)  # Output: Name: Akshay
print("Age:", s.age)    # Output: Age: 20

# Modifying properties
s.name = 'Ravi'
s.age = 25
print("Updated Name:", s.name)  # Output: Updated Name: Ravi
print("Updated Age:", s.age)    # Output: Updated Age: 25

# Trying to set a negative age
s.age = -5  # Output: Age cannot be negative
