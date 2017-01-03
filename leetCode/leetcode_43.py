class Solution(object):

    """
    Python can do it directly by str(int(num1)*int(num2))
    """

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = [0] * (len(num1) + len(num2))
        lengh = len(res)
        for i, n1 in enumerate(reversed(num1)):
            for j, n2 in enumerate(reversed(num2)):
                res[i + j] += int(n1) * int(n2)
                res[i + j + 1] += res[i + j] / 10
                res[i + j] %= 10

        pt = lengh
        while pt > 0 and res[pt - 1] == 0:
            pt -= 1

        res = res[:pt]
        return ''.join(map(str, res[::-1] or [0]))
