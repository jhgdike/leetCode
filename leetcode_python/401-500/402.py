class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        for i in num:
            while stack and k and i < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(i)
        if k:
            stack = stack[:-k]
        return ''.join(stack).lstrip("0") or "0"


print(Solution().removeKdigits("10200", 1))
print(Solution().removeKdigits("10", 1))
print(Solution().removeKdigits("10200", 2))
print(Solution().removeKdigits("10", 2))
print(Solution().removeKdigits("1432219", 3))
print(Solution().removeKdigits("10", 2))
print(Solution().removeKdigits("9", 1))
