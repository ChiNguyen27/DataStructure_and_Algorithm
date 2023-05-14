# O(1) - Constant time
# the no. of operation do not depend on the size of the input and are always constant.

import time

array_small = ['nemo' for i in range(10)]
array_medium = ['nemo' for i in range(100)]
array_large = ['nemo' for i in range(100000)]

def finding_nemo(array,i):
    t0 = time.time()
    print(array[0]) #O(1) operation
    print(array[i]) #O(1) operation
    t1 = time.time()
    print(f'Time taken ={t1 - t0}')

i=9
finding_nemo (array_small,i)
finding_nemo (array_medium,i)
finding_nemo (array_large,i)

#Note
# Time taken in all 3 case would be 0.0 seconds because we are only extracting the first and second elements of the arrays
# We are not looping over the entire array
# We are performing two O(1) operations, which is equal to O(2)
# Any constant number can be considered as 1. There we can say this function is O(1) -- constant time complexity 