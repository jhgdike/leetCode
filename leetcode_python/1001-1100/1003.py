class Solution(object):
    def isValid(self, S):
        """
        :type S: str
        :rtype: bool
        """
        stack = []
        for s in S:
            if s == 'c':
                if len(stack) < 2:
                    return False
                if stack[-1] == 'b' and stack[-2] == 'a':
                    stack.pop(),stack.pop()
            else:
                stack.append(s)
        return not stack


for s in ["abc", "aabcbc", "abcabc", "abcabcababcc"]:
    print(Solution().isValid(s))
