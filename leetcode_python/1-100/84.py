class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        left = [0] * n
        right = [n-1] * n
        stack = []
        ans = 0
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                # right[stack[-1]] = i-1  # 优化后的方法。此时可以确定stack[-1]的right值
                ans = max(ans, (i-stack[-1]) * heights[stack.pop()])
                # stack.pop()
            # left[i] = 0 if not stack else stack[-1] + 1
            stack.append(i)
        # right = [0] * n
        # stack = []
        # for i in range(n - 1, -1, -1):
        #     if not stack or heights[i] > heights[stack[-1]]:
        #         right[i] = i
        #     else:
        #         while stack and heights[stack[-1]] >= heights[i]:
        #             stack.pop()
        #         right[i] = n - 1 if not stack else stack[-1] - 1
        #     stack.append(i)
        # ans = 0
        # for i in range(n):
        #     ans = max(ans, (right[i] - left[i]+1) * heights[i])
        return ans


class Solution2(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        left = [0] * n
        right = [n-1] * n
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                right[stack[-1]] = i-1  # 优化后的方法。此时可以确定stack[-1]的right值
                stack.pop()
            left[i] = 0 if not stack else stack[-1] + 1
            stack.append(i)
        ans = 0
        for i in range(n):
            ans = max(ans, (right[i] - left[i]+1) * heights[i])
        return ans


s = Solution()
print(s.largestRectangleArea([2, 1, 5, 6, 2, 3]))
print(s.largestRectangleArea([2,4]))
