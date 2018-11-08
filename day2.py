# Given an array of integers, return a new array such that each element at index i of the new array is the
# product of all the numbers in the original array except the one at i. Solve it without using division and in O(n) time.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
# If our input was [3, 2, 1], the expected output would be [2, 3, 6]
#

import numpy as np


arr = [1,2,3,4,5]

arr_out = []

for i, each in enumerate(arr):

    arr_out.append(np.prod(arr)//arr[i]) # divide summed product of whole array by element i to get answer.
    # O(n) time - one loop. could go faster maybe w/ lamdba function?


print(arr_out)