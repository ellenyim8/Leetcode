# 918) Maximum Sum Circular Subarray
from collections import List 

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadene(nums):
            max_end_here = max_so_far = nums[0]

            for i in range(1, len(nums)):
                max_end_here = max(max_end_here + nums[i], nums[i])
                max_so_far = max(max_so_far, max_end_here)

            return max_so_far

        # case 1) max subarray within array 
        max_sum_std = kadene(nums)
        # case 2) max subarray involving wrapping around
        total = sum(nums)
        invert_nums = [-x for x in nums]
        max_sum_wrapped = total + kadene(invert_nums)

        if max(nums) <= 0:
            return max_sum_std
        
        return max(max_sum_std, max_sum_wrapped)

        
