class Solution:
    def singleNumber(self, nums):
        num = nums[0]
        for i in range(1, len(nums)):
            num ^= nums[i]

        return num


nums = [2,2,1]
print(Solution().singleNumber(nums))

nums = [4,1,2,1,2]
print(Solution().singleNumber(nums))

nums = [1]
print(Solution().singleNumber(nums))

nums = [-1]
print(Solution().singleNumber(nums))
