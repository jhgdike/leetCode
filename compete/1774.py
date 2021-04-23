class Solution(object):
    def closestCost(self, baseCosts, toppingCosts, target):
        """
        :type baseCosts: List[int]
        :type toppingCosts: List[int]
        :type target: int
        :rtype: int
        """
        d = set(baseCosts)
        for top in toppingCosts:
            nd = set()
            for item in d:
                nd.add(item)
                nd.add(item+top)
                nd.add(item+top*2)
            d = nd
        ans = -20000
        for item in d:
            if abs(item-target) < abs(ans-target):
                ans = item
        return ans


print(Solution().closestCost([1,7],[3,4],10))


