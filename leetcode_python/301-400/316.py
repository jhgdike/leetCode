class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        in_stack = [False] * 26
        left = [0] * 26
        aindex = ord('a')
        for i in s:
            left[ord(i)-aindex] += 1
        for i in s:
            index = ord(i) - aindex
            left[index] -= 1
            if not in_stack[index]:
                while stack and i < stack[-1] and left[ord(stack[-1])-aindex] != 0:
                    in_stack[ord(stack.pop())-aindex] = False
                stack.append(i)
                in_stack[index] = True
        return ''.join(stack)


s = Solution()
print(s.removeDuplicateLetters("bcabc"))
print(s.removeDuplicateLetters("cbacdcbc"))
print(s.removeDuplicateLetters("cdadabcc"))
print(s.removeDuplicateLetters("cdadabcc"))
