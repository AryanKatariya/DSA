'''Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3].
2 is the missing number in the range since it does not appear in nums.

Example 2:
Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2].
2 is the missing number in the range since it does not appear in nums.

Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9].
8 is the missing number in the range since it does not appear in nums.'''

def missingNumber(nums):
    max_number = max(nums) + 1
    range_sum = sum([i for i in range(max_number)])
    nums_sum = sum(nums)
    missing_number = range_sum - nums_sum
    if missing_number not in nums:
        return missing_number
    else:
        return max_number

nums = [9,6,4,2,3,5,7,0,1]
print(missingNumber(nums))
