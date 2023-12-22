# 238) Product of Array Except Self

from collections import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [0] * n
        right = [0] * n
        left_mult = 1
        right_mult = 1

        for idx in range(n):
            j_idx = -idx - 1

            left[idx] = left_mult
            left_mult *= nums[idx]

            right[j_idx] = right_mult
            right_mult *= nums[j_idx]

        answer = []
        for l, r in zip(left, right):
            answer.append(l * r)

        return answer

        # answer = []

        # for i in range(len(nums)):
        #     m = 1
        #     for j in range(len(nums)):
        #         if i != j:
        #             m *= nums[j]
        #     answer.append(m)

        # return answer
    