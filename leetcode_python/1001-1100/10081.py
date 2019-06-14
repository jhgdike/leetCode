"""
不对，还没做出来
"""

class Solution(object):
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


_ = ["cbaacabcaaccaacababa", "cdadabcc", "ddeeccde"]
print(Solution().smallestSubsequence("cbaacabcaaccaacababa"))
