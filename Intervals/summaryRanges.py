# 228) Summary Ranges
from collections import List 

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []

        if len(nums) == 0:
            return []
        
        st = nums[0]
        ed = nums[0]
        n = len(nums)

        for i in range(1, n):
            if nums[i] == ed + 1:
                ed = nums[i]
                # res.append(st)
            else:
                res.append((st, ed))
                st = ed = nums[i]
            
        res.append((st, ed))

        return [str(st) if st == ed else f"{st}->{ed}" for st, ed in res]

