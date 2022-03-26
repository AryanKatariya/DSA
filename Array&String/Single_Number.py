'''
Input: nums = [4,1,2,1,2]
Output: 4
'''
def singleNumber(nums):
        s = set()
        for num in nums:
            if num in s:
                s.remove(num)
            else:
                s.add(num)
        return s

nums = [4,1,2,1,2]
print(singleNumber(nums))
