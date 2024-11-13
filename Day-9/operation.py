#union : combine two different set (set1 & set2)
set1={1,2,4,5}
set2={2,4,2,4,9}
print(set1|set2)
print(set1.union(set2))

# intersection : return the common elements from set
set_1={"hello","hi"}
set_2={"hello","hye","bye"}
print(set_1 & set_2)

# difference : use to un common element

set_1={"hello","hi"}
set_2={"hello","hye","bye"}
print(set_1 - set_2)
print(set_2-set_1)

# symmetric : remove the common value from the set
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
sym_diff = set1.symmetric_difference(set2)
sym_diff1=set2.symmetric_difference(set1)
print("Symmetric Difference 1:", sym_diff)
print("Symmetric Difference 2:", sym_diff1)
print(set1^set2)

# Frozenset : these are the imutable version of the sets, once created, we cant modify, add or remove the item
frozenset=frozenset([1,2,3])
print(frozenset)
#
# frozenset.add(14)
# print(frozenset)


#list conversion into set
mylist = [1, 2, 2, 4, 5]
myset = set(mylist)
print(myset)

