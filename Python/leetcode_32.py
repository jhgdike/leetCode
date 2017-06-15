class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        ans = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                else:
                    stack.append(i)

        if not stack:
            ans = len(s)
        else:
            ans = len(s) - stack[-1] - 1
            for i in range(1, len(stack)):
                ans = max(ans, stack[i] - stack[i-1] - 1)
            ans = max(ans, stack[0])

        return ans
