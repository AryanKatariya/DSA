'''Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.'''

def thridMax(nums):
    arr = list(set(nums))
    if len(arr) < 3:
        return max(arr)

    arr.remove(max(arr))
    arr.remove(max(arr))
    return max(arr)
