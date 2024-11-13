# set does not allow duplicaate value, {} we used to declare the set value ,
# it is in unordered collection (does not support indexing)
# set is mutuable

my={1,2,43,2,4}
print("element in the list are :",my)

# add element in the list
my_set={1,2,43,2,5}
my_set.add(4)
print(my_set)

# remove element from the set
my_set.remove(43)
print(my_set)

set_my={2,"hello",3,8}
print(set_my)


# example of set creating
myset_1={"apple","banana","cherry"}
print(myset_1)

# accessing the elements from set
#  index- not apply here-------------------------- PTR
# for loop we can use


 # add : when we want to add only single item
myset_1.add("kiwi")
print(myset_1)

# update : when we want to add multiple items
myset_1.update(my_set)
print(myset_1)


# remove method : remove through an error message if element not in the list
myset_1.remove("kiwi")
print(myset_1)


# discard : remove element if exists in the set or print the value
myset_1.discard("apple")
print(myset_1)


# clear all the element from the memory
myset_1.clear()
print(myset_1)

# delete the complete set
print(my_set)
del my_set


