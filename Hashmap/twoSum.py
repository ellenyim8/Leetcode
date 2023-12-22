# 1) Two Sum
from collections import List 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        prev = {}
        
        for i, j in enumerate(nums):
            diff = target - j
            if diff in prev:
                return [prev[diff], i] 
            prev[j] = i 

