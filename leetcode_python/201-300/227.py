class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        num = 0
        operation = {
            '+': lambda o: stack.append(o),
            '-': lambda o: stack.append(-o),
            '*': lambda o: stack.append(stack.pop() * o),
            '/': lambda o: stack.append(int(stack.pop() / float(o))),
        }
        operator = '+'
        for i in s+'+':
            if 48 <= ord(i) <= 57:
                num = num * 10 + ord(i) - 48
            else:
                if i in operation:
                    operation[operator](num)
                    operator = i
                    num = 0
        return sum(stack)

    def test(self):
        r = 0
        stack = []
        ans = 0
        s = s.strip()
        while r < len(s):
            l = r
            while r < len(s) and 48 <= ord(s[r]) <= 57:
                r += 1
            stack.append(int(s[l:r]))
            if len(stack) > 2 and stack[-2] in '*/':
                i2 = stack.pop()
                al = stack.pop()
                i1 = stack.pop()
                if al == '*':
                    stack.append(i1 * i2)
                else:
                    stack.append(int(i1 / i2))
            while r < len(s) and s[r] == ' ':
                r += 1
            if r >= len(s):
                break
            stack.append(s[r])
            r += 1
            while r < len(s) and s[r] == ' ':
                r += 1
        if len(stack) >= 1:
            ans = stack[0]
            l = 1
            while l < len(stack):
                if stack[l] == '+':
                    ans += stack[l + 1]
                else:
                    ans -= stack[l + 1]
                l += 2
        return ans


print(Solution().calculate('3+2*2'))
print(Solution().calculate('3/2'))
print(Solution().calculate(' 3+5 / 2 '))
print(Solution().calculate("14-3/2"))
