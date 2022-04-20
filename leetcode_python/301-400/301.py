
# 1. 计算出要删除的左右括号数
# 2.回溯，移除多余的括号
# 3. 判断结果是否有效
def isValid(s):
    stack = []
    for i in s:
        if stack and i == ')' and stack[-1] == '(':
            stack.pop()
            continue
        if i != '(' and i != ')':
            continue
        stack.append(i)
    return len(stack) == 0

def backTrack(s, start, lr, rr):
    # 完成条件
    if lr == 0 and rr == 0:
        if isValid(s):
            res.append(s)
        return
    for i in range(start, len(s)):
        if i > start and s[i] == s[i - 1]:
            continue
        if s[i] == '(' and lr > 0:
            backTrack(s[:i]+s[i+1:], i, lr - 1, rr)
        if s[i] == ')' and rr > 0:
            backTrack(s[:i]+s[i+1:], i, lr, rr - 1)

s = '()())()'
# 计算要删除的括号数
res = []
lr, rr = 0, 0
for i in s:
    if i == '(':
        lr += 1
    if i == ')':
        if lr > 0:
            lr -= 1
        else:
            rr += 1
backTrack(s, 0, lr, rr)
print(res, lr, rr)
