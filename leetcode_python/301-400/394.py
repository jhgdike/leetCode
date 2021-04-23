class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for i in s:
            if 'a' <= i <= 'z' or i == '[':
                stack.append(i)
            elif '0' <= i <= '9':
                if stack and isinstance(stack[-1], int):
                    stack[-1] = stack[-1] * 10 + int(i)
                else:
                    stack.append(int(i))
            else:
                cur = []
                while True:
                    p = stack.pop()
                    if p == '[':
                        break
                    cur.append(p)
                n = 1
                if stack and isinstance(stack[-1], int):
                    n = stack.pop()
                stack.append(''.join(reversed(cur))*n)

        return ''.join(stack)


print(Solution().decodeString("3[a]2[bc]"))
print(Solution().decodeString("3[a2[c]]") == "accaccacc")
print(Solution().decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef")
print(Solution().decodeString("abc3[cd]xyz") == "abccdcdcdxyz")
