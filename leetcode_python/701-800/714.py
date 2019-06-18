class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        total = 0
        cur_max = cur_min = prices[0]
        for i in range(1, len(prices)):
            if cur_min > prices[i]:
                if (cur_min + fee) < cur_max:
                    total += cur_max - cur_min - fee
                cur_max = cur_min = prices[i]
            else:
                cur_max = max(cur_max, prices[i])
                if i == len(prices) - 1:
                    total += max(cur_max - cur_min - fee, 0)
                else:
                    if (cur_min + fee) < cur_max and cur_max - fee >= prices[i]:
                        total += cur_max - cur_min - fee
                        cur_min = cur_max = prices[i]
        return total


prices = [2,1,4,4,2,3,2,5,1,2]

fee = 1
print(Solution().maxProfit(prices, fee))
