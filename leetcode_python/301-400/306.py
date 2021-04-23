class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if len(num) < 3:
            return False
        stack = []

        def dfs(n):
            if n == len(num):
                return True
            if n == 0:
                for i in range(len(num)//2):
                    if num[0] == '0' and i > 0:
                        return False
                    stack.append(num[:i+1])
                    res = dfs(i+1)
                    stack.pop()
                    if res:
                        return True
                return False
            elif len(stack) == 1:
                for i in range(1, (len(num)-n)//2+1):
                    if num[n] == '0' and i > 1:
                        return False
                    stack.append(num[n:n+i])
                    res = dfs(n+i)
                    stack.pop()
                    if res:
                        return res
                return False
            else:
                s = str(int(stack[-1])+int(stack[-2]))
                if num[n:n+len(s)] == s:
                    stack.append(num[n:n+len(s)])
                    res = dfs(n+len(s))
                    stack.pop()
                    if res:
                        return res
                return False

        return dfs(0)

from collections import OrderedDict
print(Solution().isAdditiveNumber("112358"))
print(Solution().isAdditiveNumber("199100199"))
print(Solution().isAdditiveNumber("0235813"))
print(Solution().isAdditiveNumber("123"))
print(Solution().isAdditiveNumber("101"))
print(Solution().isAdditiveNumber("199111992"))
print(Solution().isAdditiveNumber("101"))
