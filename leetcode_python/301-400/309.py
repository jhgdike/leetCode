class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        f0 = -prices[0]  # 持有股票
        f1 = f2 = 0  # 不持有--冷冻期，非冷冻期
        for i in range(1, len(prices)):
            newf0 = max(f0, f2-prices[i])
            newf1 = f0+prices[i]
            newf2 = max(f1, f2)
            f0 = newf0
            f1 = newf1
            f2 = newf2
        return max(f1, f2)
