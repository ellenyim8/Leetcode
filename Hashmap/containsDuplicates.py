# 219) Contains Duplicates II
from collections import List 

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = dict()
        
        for index, number in enumerate(nums):
            if number in hashmap and abs(index - hashmap[number]) <= k:
                return True

            hashmap[number] = index

        return False

