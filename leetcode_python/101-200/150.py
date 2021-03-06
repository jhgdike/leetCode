class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for t in tokens:
            if t not in '+-*/':
                stack.append(int(t))
            else:
                b = stack.pop()
                a = stack.pop()
                if t == '+':
                    stack.append(a + b)
                elif t == '-':
                    stack.append(a-b)
                elif t == '*':
                    stack.append(a*b)
                else:
                    stack.append(int(1.0*a/b))
            # print(stack)
        return int(stack[-1])


print(Solution().evalRPN(["2","1","+","3","*"]))  # 9
print(Solution().evalRPN(["4", "13", "5", "/", "+"]))  # 6
print(Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))  # 22
print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))  # 22
