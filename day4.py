# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
#
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

import numpy as np



test_arr = np.array([3, 4, -1, 1])
# test_arr = np.array([1,2,0])

arr = test_arr[np.where(test_arr > 1)] #lose negatives and 1's (so when minus 1 gives smallest ommited pos int)
min_int = np.min(arr)-1 #coarse answer assuming minimum value is not 1.
for i in range(0,len(test_arr)):
    if min_int in test_arr:  ###if not fast can convert to set for ish O(1) performance here.  rest O(n)
        print(min_int)

        min_int = min_int+1
        print('dsdsd')
    else:
        print(min_int)
        break

