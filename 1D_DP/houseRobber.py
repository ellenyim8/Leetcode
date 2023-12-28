# 198 - House Robber

class Solution:
    def rob(self, nums) -> int:
        rob1, rob2 = 0, 0

        for num in nums:
            tmp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = tmp

        return rob2

