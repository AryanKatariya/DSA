def maxSubArray(nums):
        if max(nums) < 0:
            return max(nums)
        global_max = 0
        local_max = 0
        for n in nums:
            local_max = max(0, local_max + n)
            global_max = max(global_max, local_max)
        return global_max
