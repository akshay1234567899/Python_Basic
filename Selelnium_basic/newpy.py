import arr
from fontTools.misc.cython import returns


def duplicate(arr):
    duplicate=[]
    seen=set()

for num in arr:
    if num in seen and num  not in duplicate:
        duplicate.append(num)
        seen.add(num)
# return duplicate

arr=[1,2,3,6,1,0,4]
print(duplicate(arr))