# 162) find peak element
class Solution:
    def findPeakElement(self, nums):
        L, R = 0, len(nums) - 1

        while L < R:
            mid = L + (R - L) // 2

            if nums[mid] > nums[mid + 1]:
                # look in left
                R = mid
            else:
                # look in right
                L = mid + 1

        return L

        
