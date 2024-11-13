# numpy : stand for numerical python
# powerful library which is mostly use in data analysis and scientific calculation etc.
# in Numpy, an array is the fundamental object.
# from array import array

#           Array                               List
#  1.store homogenours data             store hetrogenous data

#  2. Element of array are store in     Element of array are store in
#     contineous memory location            diff memory location

#  3. Searching consume less time       Searching consume more time
#  4. Static                             resize (delete or insert the element)
#  5. Element wise operation             Don't support Element wise operation
#      (Homogenous data)                     (hetrogenous data)

import numpy as np
list=[1,2,3,4,3,4]
array_1=np.array(list)
print(array_1)