# 191 - number of 1 bits

class Solution:
    def hammingWeight(self, n):
        count = 0
        # loop through all bits check if bit is set and it yes then increment count
        while n:
            count += n & 1
            n >>= 1
        return count

        # O(log n) time, O(1) space
        

# n = 00000000000000000000000000001011;
# print(Solution().hammingWeight(n))

# n = 00000000000000000000000010000000;
# print(Solution().hammingWeight(n))
