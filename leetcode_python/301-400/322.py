class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        dp = [0] * (amount + 1)
        for i in range(1, amount+1):
            if i in coins:
                dp[i] = 1
            else:
                for coin in coins:
                    if i > coin and dp[i-coin] and (dp[i] == 0 or dp[i-coin]+1 < dp[i]):
                        dp[i] = dp[i-coin]+1
        return dp[-1] or -1


print(Solution().coinChange([1,2,5], 11))
print(Solution().coinChange([2,], 3))
print(Solution().coinChange([1], 0))
print(Solution().coinChange([1], 1))
print(Solution().coinChange([1], 2))
print(Solution().coinChange([1,2,5], 11))
print(Solution().coinChange([1,2,5], 11))
