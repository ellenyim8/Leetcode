# 201 - Bitwise AND of numbers Range

class Solution:
    def rangeBitwiseAnd(self, left, right):
        res = 0

        # left = 5, right = 7
        # shift 5 to right 
        # shift 7 to right 
        # return left after shifting left by res times
        while left < right:
            left >>= 1
            right >>= 1
            res += 1
        
        return left << res

        
# left, right = 5, 7
# print(Solution().rangeBitwiseAnd(left, right)) # 4

# left, right = 0, 0
# print(Solution().rangeBitwiseAnd(left, right)) # 0

# left, right = 1, 2147483647
# print(Solution().rangeBitwiseAnd(left, right)) # 0

        
