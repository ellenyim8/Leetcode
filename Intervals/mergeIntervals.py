# 56) Merge Intervals
from collections import List 

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0 or len(intervals) == 1:
            return intervals

        intervals.sort()
        results = []
        for i in intervals:
            if not results or i[0] > results[-1][1]:
                results.append(i)
            else:
                results[-1][1] = max(results[-1][1], i[1])
        
        return results
