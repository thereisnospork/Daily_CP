# Given a list of integers, write a function that returns the largest sum of
# non-adjacent numbers. Numbers can be 0 or negative.
#
# For example, [2, 4, 6, 8] should return 12, since we pick 4 and 8. [5, 1, 1, 5]
# should return 10, since we pick 5 and 5.

import numpy as np

testlist = [1,2,3,4,53,54,5,6,6,7,5]

def largest_non_adj(nums):
    """takes test list (iterable of numerics) and returns sum of largest 2 non adjacent
    numbers"""
    max_num = np.max(nums)
    max_index = np.argmax(nums)
    nums.pop(max_index) #num
    try:
        nums.pop(max_index-1) #num behind
        nums.pop(max_index-1) #num in front (no where num behind was)
    except Exception: ##incase num is at end not to choke
        None
    ans = max_num + np.max(nums)
    print(ans)
    return(ans)

largest_non_adj(testlist)




