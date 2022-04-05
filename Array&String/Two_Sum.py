def twoSum(nums,target):
    prevMap = {}

    for i,n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff],i]
        prevMap[n] = i

nums = [2,7,9,11,5]
print(twoSum(nums,9))
