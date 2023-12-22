# 134) Gas Station

from collections import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        res = 0
        tank = 0
        used = 0

        # try to begin at starting index
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            used += gas[i] - cost[i]

            if used < 0:
                used = 0
                res = i + 1 # go to next index

            
        return -1 if tank < 0 else res

