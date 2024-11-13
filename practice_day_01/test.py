# 3 Write a Python code that takes a dictionary and returns the sum of all its values.
# from exceptionhandling.exception_demo import result
from exceptionhandling.exception_demo import result


# def dict_input(input_dict):
#     return sum(input_dict.values())
# example_dict ={
#     "test":10,
#     "data":20,
#     "mac":30
# }
# result=dict_input(example_dict)
# print("result of dictionary function:",result)



# 4.Write a Python code that converts a tuple of numbers to a list, appends a given number to the list
# and then converts it back to a tuple.

def tuple_to_list(input_value,number_to_append):
    list_1=list(input_value)
    list_1.append(number_to_append)
    result_tuple=tuple(list_1)
    return result_tuple

example_list=(1,2,3)
number=4
result=tuple_to_list(example_list,number)
print("convert tuple to list and vice versa",result)

# 5.Write a Python code that removes the minimum and maximum values from a set.

# 6.Return the symmetric difference of two sets.

# 7.Write a Python function that finds and returns the index of all occurrences of a specified element in a list
#  using the  method. If the element is not found, return.

