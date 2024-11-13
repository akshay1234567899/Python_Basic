# Tuple :
# # Slicing :
# mytuple=("apple","mango","banana","cherry","orange","melon")
# #  add element on tuple
#
# mytuple.append("kisi")
# print(mytuple)
# output : AttributeError: 'tuple' object has no attribute 'append'


# Add element in the list :
# append
# insert

# Convert list in tuple
# tuple----list(modify)-----tuple

mytuple=("apple","mango","banana","cherry","orange","melon")
my_list=list(mytuple)
print(my_list)

my_list[0]="kiwi"
print(my_list)

# reading the tuple from for loop
mytuple = ("apple", "cherry", "kiwi", "orange", "stop")
num = input("Enter the query: ")
if num in mytuple:
    print("Element exists in the tuple:", num)
else:
    print("Element does not exist in the tuple.")

#     tuple 1= 1,2,3,4,5
#     tuple 2= 4,2,5,2
#     tuple3 =tuple1+tuple2
#     tuple1==tuple2






