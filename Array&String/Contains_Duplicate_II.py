'''Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false'''

def containsNearbyDuplicateOpt(nums,k):
    indices = {}
    for ind,key in enumerate(nums):
        if(key in indices and ind-indices[key]<=k):
            return True
        indices[key] = ind
    return False

def containsNearbyDuplicate(nums,k):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                continue
            if nums[i] == nums[j] and abs(j-i) <= k:
                return True
    return False

nums = [1,0,1,1]
k = 1
print(containsNearbyDuplicate(nums,k))
print(containsNearbyDuplicateOpt(nums,k))
