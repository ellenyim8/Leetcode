# 300) longest increasing subsequence

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        DP
        """

        # nums = [10 9 2 5 3 7 101 18]
        # j=1 to len(nums)-1, i=0 to j 
        # lis = [1 for i in range(len(nums))] - base case for substr len of 1
        # loop from j=1 to len(nums)-1
        #   loop from i=0 to j
        #       if nums[j] > nums[i] and lis[j] < lis[i] + 1:
        #            lis[j] = lis[i] + 1
        # maxval = lis[0]
        # loop through lis
        #   if lis[ele] > maxval:
        #       maxval = lis[ele]
        # return maxval

        lis = [1 for i in range(len(nums))]

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j] and lis[i] < lis[j] + 1:
                    lis[i] = max(1, lis[j] + 1)
        
        print(lis)
        max_val = lis[0]
        for val in lis:
            if val > max_val:
                max_val = max(val, max_val)

        return max_val

        
