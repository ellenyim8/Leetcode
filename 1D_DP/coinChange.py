# Leetcode 322 - Coin change 

class Solution:
    def coinChange(self, coins, amount):
        s = [999999999] * (amount + 1)

        s[0] = 0

        for curr_amt in range(1, amount + 1):
            for coin in coins:
                if curr_amt - coin >= 0:
                    s[curr_amt] = min(s[curr_amt], s[curr_amt - coin] + 1)

        if s[amount] != 999999999:
            return s[amount]
        else:
            return -1


coins = [1, 2, 5]
amount = 11
print(Solution().coinChange(coins, amount))

coins = [2]
amount = 3
print(Solution().coinChange(coins, amount))

coins = [1] 
amount = 0
print(Solution().coinChange(coins, amount))

