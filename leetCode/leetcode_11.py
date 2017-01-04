class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = water = 0
        j = len(height) - 1
        while i < j:
            h = min(height[i], height[j])
            water = max(water, h * (j - i + 1))
            while height[i] <= h and i < j: i += 1
            while height[j] <= h and i < j: j -= 1
        return water
