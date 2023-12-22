# 169) Majority Element

class Solution:
    def majorityElement(self, nums) -> int:
        d = dict()
        ans = 0
        for num in nums:
            if num not in d:
                d[num] = 1 
            else:
                d[num] += 1 

        for k, v in d.items():
            if v > int(len(nums) / 2):
                ans = k 
        
        return ans 
