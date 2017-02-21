class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n <= 2:
            return 0

        max_height, max_index = -1, 0
        for i, x in enumerate(height):
            if x > max_height:
                max_height = x
                max_index = i

        area = 0
        tall = 0
        for i in range(max_index + 1):
            if tall > height[i]:
                area += (tall - height[i])
            else:
                tall = height[i]

        tall = 0
        for i in range(n - 1, max_index - 1, -1):
            if tall > height[i]:
                area += (tall - height[i])
            else:
                tall = height[i]
        return area


class Solution2(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n <= 2:
            return 0

        max_height, max_index, sum_h = -1, 0, 0
        for i, x in enumerate(height):
            if x > max_height:
                max_height = x
                max_index = i
            sum_h += x

        area = 0
        tall = 0
        for i in range(max_index):
            if tall < height[i]:
                area += (max_index - i) * (height[i] - tall)
                tall = height[i]

        tall = 0
        for i in range(n - 1, max_index, -1):
            if tall < height[i]:
                area += (i - max_index) * (height[i] - tall)
                tall = height[i]
        return area - sum_h + max_height
