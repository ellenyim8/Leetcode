# 167) Two sum II - input array is sorted 

from collections import List 
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L = 0
        R = len(numbers) - 1
        index = []

        while L <= R:
            if numbers[L] + numbers[R] == target:
                #print(L, ' ', R)
                index.append(L+1)
                index.append(R+1)
                break
            elif numbers[L] + numbers[R] < target:
                L += 1
            elif numbers[L] + numbers[R] > target:
                R -= 1

        return index
    