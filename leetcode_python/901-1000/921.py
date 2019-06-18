class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        ans = 0
        for s in S:
            if s == '(':
                stack.append(s)
            else:
                if not stack or stack[-1] != '(':
                    ans += 1
                else:
                    stack.pop()
        return ans + len(stack)


S = "()))(("
print(Solution().minAddToMakeValid(S))
