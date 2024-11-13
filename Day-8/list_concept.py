# list=["apple","car","mango"]
# print(list)
# # with the hlep of loop
# for i in list:
#     print(i)
import string
from tokenize import String

from python_program.countthenumber import count

# example : check if item is exist in the list or not
mylist=["apple","mango","cherry"]
if "mango" in mylist:
    print("item available")
else:
    print("item not available in the list")

#compare with for loop
# for i in mylist:


# example list of length of list
print(len(mylist))

# append method
mylist=["my","python","course"]
mylist.append("pratice")
print(mylist)

# insert method
mylist.insert(1,"car")
print(mylist)

# how to remove item from the list
# pop= delete,
mylist=["my","python","course"]
mylist.pop(0)
print(mylist)

# Delete the entire list from the array
Set_list=["mylist","python","course"]
del Set_list
# print(Set_list)

# Clear the list
cl_list=["mylist","banana","mango"]
cl_list.clear()
print(cl_list)

# copy list
# list method : used to copy of one element to another element
cl_list=["mylist","banana","mango"]
mylist=list(cl_list)
print(mylist)

# coppy
Set_list=["mylist","python","course"]
cl_list=["mylist","banana","mango"]
cl_list=Set_list.copy()
print(cl_list)


# using operator
list1=["akshay","manish","dhankhar"]
list2=[10,20,30]
list3=list1+list2
print(list3)


# append method
for i in list1:
    list2.append(i)
print(list2)

# extend
list1=['a','b','c']
list2=[10,20,30,40,50]
list1.extend(list2)
print(list1)

# how to take input from the user in list
# user_input=input("Enter the elements of list")
# a=input().split(",")
# print(a)

# list map func (number format)
# enter_list=list(map(int,(input("enter the element of list").split(","))))
# print(enter_list)

# reading a list of string from userinput
# enter_string=(input("Enter the string value from the user").split(" "))
# print(enter_string)

# read input from the user, split by comma and convert to a list of string
# user_input=input("Enter the element of list")
# item=[item.strip() for item in user_input.split(",")]
# print(item)

# sorting in py
# count
# Taking input from the user and converting it into a list of integers
elements = list(map(int, input("Enter the numbers: ").split()))
for i in elements:
    print(i)

# ----------------------------------------------------------------------------------
# touple : which are ordered and unchangeable we are going to use the round bracket
# mytuple=(10,20,30,40,50)
# print(mytuple)
# ---------------------------------------------------------------------------------
# mytuple1=("apple","cherry","kiwi","orange","stop")
# print(mytuple1[2:5])
# print(mytuple1[-1:-4:1])

