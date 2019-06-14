class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        while len(stones) > 1:
            stones.sort()
            a, b = stones[-2:]
            stones.pop()
            if a > b:
                stones[-1] = a - b
            elif a < b:
                stones[-1] = b - a
            else:
                stones.pop()
        return stones and stones[0] or 0
