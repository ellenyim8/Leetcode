# 39) Combination Sum

from collections import List 

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # pointer points to one leement and once that element is used up, then ptr will move
        # recursion tree 
        
        # time complexity: 2^n
        
        res = []
        
        def dfs(i, curr, total):
            # i - index, cur = list[] , total = current total sum 
            # base case
            if total == target:
                res.append(curr.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            # candidates[i]
            curr.append(candidates[i])
            dfs(i, curr, total+candidates[i])
            curr.pop()
            dfs(i+1, curr, total)
            
        dfs(0, [], 0)
        return res
            
