class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        degree = 1
        for p in preorder.split(','):
            if degree == 0:
                return False
            if p == '#':
                degree -= 1
            else:
                degree += 1
        return not degree

    def test(self, preorder):
        if not preorder or preorder == '#':
            return True
        preorder = preorder.split(',')
        if preorder[0] == '#':
            return False
        stack = []
        i = 0
        while i < len(preorder):
            if preorder[i] != '#':
                stack.append(preorder[i])
                i+=1
            else:
                stack.append('#')
                i+=1
                while i <= len(preorder) and stack[-1] == '#':
                    if len(stack) >= 2 and stack[-2] == '#':
                        stack.pop()
                        stack.pop()
                        if len(stack) == 0:
                            return False
                        stack[-1] = '#'
                    elif i < len(preorder) and preorder[i] == '#':
                        stack.pop()
                        if len(stack) == 0:
                            return False
                        stack[-1] = '#'
                        i+=1
                    else:
                        break
        return len(stack) == 1 and stack[0] == '#'


print(Solution().isValidSerialization('9,3,4,#,#,1,#,#,2,#,6,#,#'))
print(Solution().isValidSerialization('9,#,#,1'))
print(Solution().isValidSerialization("1,#,#,#,#"))
print(Solution().isValidSerialization("9,9,91,#,#,9,#,49,#,#,#"))
print(Solution().isValidSerialization("1,#,#"))
print(Solution().isValidSerialization("1,#"))
print(Solution().isValidSerialization("1,#"))

