# 34) Find First and Last position of element in sorted array

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        result = []
        first = 0
        last = 0
        
        for i in range(len(nums)):
            if (nums[i] == target):
                first = i
                result.append(first)
                break
        else:
            first = -1
            result.append(first)
            
                
        for j in range(len(nums)-1, -1, -1):
            if nums[j] == target:
                last = j
                result.append(last)
                break
                
        else:
            last=-1
            result.append(last)
            
                
        return result 
    
        
