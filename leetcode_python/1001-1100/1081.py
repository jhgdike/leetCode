"""
不对，还没做出来
"""


class Solution(object):
    def smallestSubsequence(self, text):
        stack = []
        for i, t in enumerate(text):
            if t in stack:
                continue
            while stack and t < stack[-1] and text.find(stack[-1], i) != -1:
                stack.pop()
            stack.append(t)
        return ''.join(stack)


class Solution2(object):
    """不对，还没做出来"""
    def smallestSubsequence(self, text):
        """
        :type text: str
        :rtype: str
        """
        l = len(text)
        seq = ""
        i = l
        while i > 0:
            i -= 1
            if i != l - 1 and text[i] == text[i+1]:
                continue
            t = text[i]
            if t not in seq:
                seq = t + seq
            else:
                index = seq.index(t)
                new_seq = t + seq[:index] + seq[index+1:]
                if new_seq < seq:
                    seq = new_seq
        return seq


tests = ["cdadabcc", "cbaacabcaaccaacababa", "cdadabcc", "ddeeccde", 'leetcode', 'ecbacba']
for test in tests:
    print(Solution().smallestSubsequence(test))
