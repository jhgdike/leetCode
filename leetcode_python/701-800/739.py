class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        stack = [0]
        res = [0] * len(T)
        for i in range(1, len(T)):
            while stack and T[i] > T[stack[-1]]:
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return res


s = Solution()
nums = [73, 74, 75, 71, 69, 72, 76, 73]
print(s.dailyTemperatures(nums))
