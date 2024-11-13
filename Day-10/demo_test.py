# arr=array("i",[2,1,3,4,2])
# print(arr)
# Array : use to store similar type of element like int 1,2,3,4,4,5 .... so on. Array are more memory efficent then list when dealing

# with a large number of elements as they required.
# array : 1-D,2-D,3-D
# array=array.array(typecode,[elements])
import array as arr1

arr= arr1.array("b", [1, 2, 3, 4, 5])
print(arr)

# arr[2]=10
# print(arr)

# arr.pop() used to remove/delete last element from the arrray
# print(arr)

# remove: used to remove the element from the specific location.
# arr.pop(1)


# remove :
# arr.remove(10)
# print(arr)

# Array slicing :
# Create an array of integers
# arr = array.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Slicing examples
# print(arr[2:5])  # Output: array('i', [3, 4, 5])  (elements from index 2 to 4)
# print(arr[:3])   # Output: array('i', [1, 2, 3])  (elements from start to index 2)
# print(arr[4:])   # Output: array('i', [5, 6, 7, 8, 9, 10])  (elements from index 4 to the end)
# print(arr[::2])  # Output: array('i', [1, 3, 5, 7, 9])  (every second element)

# append : adds a new element x to the end of the array
# remove : remove the element from the occurence first
# index : find element in array with index value
# pop : delete element from last of array
# reverse : reverse the element of array

# arr = array.array('i', [1, 2, 3, 4, 5])
# arr.reverse()
# print(arr)

