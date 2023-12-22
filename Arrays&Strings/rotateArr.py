# 189) Rotate Array

class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """

        n = len(nums)
        tmp = [0] * n
        
        for i in range(n):
            tmp[(i+k) % n] = nums[i]

        for i in range(n):
            nums[i] = tmp[i]

 
        