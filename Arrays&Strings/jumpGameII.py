# 45) Jump Game II

class Solution:
    def jump(self, nums):
        def helper(nums, idx, end, dp):
            if idx == end:
                return 0

            if dp[idx] != 0:
                return dp[idx]

            min_jumps = float('inf')
            for j in range(nums[idx], 0, -1):
                if idx + j <= end:
                    min_jumps = min(min_jumps, 1 + helper(nums, idx + j, end, dp))

            dp[idx] = min_jumps
            return dp[idx]

        dp = [0 for _ in range(len(nums))]
        helper(nums, 0, len(nums) - 1, dp)
        return dp[0]

