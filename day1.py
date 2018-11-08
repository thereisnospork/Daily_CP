# Given an array of numbers, return whether any two sums to K.
#
# For example, given [10, 15, 3, 7] and K of 17, return true since 10 + 7 is 17.

import numpy as np

test_arr = np.array([1,4,5,6,43,4,5,3,7,10])

def equal_sum(arr, sum_int):
    """

    :param arr: input array of ints
    :param sum_int: input int to which we test for any two in test_arr sums to 'sum_int'
    :return: T/F
    """
    subtract = sum_int-arr
    for each in subtract:
        if each in test_arr:
            return True
    return False # only after going through full list
    # print(subtract)

a = equal_sum(test_arr, 17)
print(a)