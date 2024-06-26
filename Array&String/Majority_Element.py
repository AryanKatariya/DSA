'''Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2'''

import collections


def majorityElement(nums):
    return collections.Counter(nums).most_common(1)[0][0]
    
