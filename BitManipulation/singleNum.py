# 137 - Single Number II

class Solution:
    def singleNumber(self, nums):
        # run loop for all elements in nums
        #       maintain 2 values:
        #       ones: bits appeared 1st, 4th, 7th time, etc
        #       twos: bits appeared 2nd, 5th, 8th time, etc
        # return value of ones
        
        ones, twos = 0, 0
        # | : bitwise or- use for twos after getting bits that are both in ones and nums[i]
        # set that to twos
        for i in range(len(nums)):
            twos = twos ^ (ones & nums[i])
            ones = ones ^ nums[i]
            bit_mask = ~(ones & twos)   # bit appears third time

            # remove bits that appear third time from ones and twos
            ones &= bit_mask
            twos &= bit_mask

        return ones


# nums = [2,2,3,2]
# print(Solution().singleNumber(nums))

# nums = [0,1,0,1,0,1,99]
# print(Solution().singleNumber(nums))


