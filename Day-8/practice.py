# from Collections.list import list1
from Collections.list import list1

# mulist=["apple","mango","cherry","banana"]

# for i in range(len(mulist)):
#     print(i)

list=list((input("Enter query as per requ :").split()))
print("element of list are :")
for i in list:
    num = input("Enter the query ")
    if i in num:
     print("Element exit in the list =",i)


