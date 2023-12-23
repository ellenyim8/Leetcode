# 46) Permutations
from collections import List 
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        # one method is to backtrack
        
        # base cases (if len of nums is 0 or 1)
        if len(nums) == 0:
            return []
        
        if len(nums) == 1:
            return [nums]
        
        if not nums:
            return [[]]
        else:
            return [[nums[i]] + j for i in range(len(nums)) for j in self.permute(nums[:i] +nums[i+1:])]
        