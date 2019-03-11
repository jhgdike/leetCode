class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if not s or numRows <= 1:
            return s
        res = [''] * len(s)
        index = 0
        gap = 2 * numRows - 2
        for i in range(numRows):
            j = 0
            while i + j * gap < len(s):
                res[index] = s[i + j * gap]
                index += 1
                if i != 0 and i != numRows - 1 and (j + 1) * gap - i < len(s):
                    res[index] = s[(j + 1) * gap - i]
                    index += 1
                j += 1

        return ''.join(res)
