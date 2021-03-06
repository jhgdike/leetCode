class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        string_buffer = []
        if numerator == 0:
            return "0"
        if (numerator < 0) ^ (denominator < 0):
            string_buffer.append("-")
        numerator = abs(numerator)
        denominator = abs(denominator)
        string_buffer.append(str(numerator//denominator))
        remain = numerator % denominator
        if remain == 0:
            return ''.join(string_buffer)
        string_buffer.append('.')
        rd = dict()
        while remain:
            if remain in rd:
                string_buffer.insert(rd[remain], '(')
                string_buffer.append(')')
                break
            rd[remain] = len(string_buffer)
            remain *= 10
            string_buffer.append(str(remain // denominator))
            remain %= denominator
        return ''.join(string_buffer)


print(Solution().fractionToDecimal(1, 3))
print(Solution().fractionToDecimal(-1, 3))
print(Solution().fractionToDecimal(1, 2))
print(Solution().fractionToDecimal(6, 3))
print(Solution().fractionToDecimal(1, 4))
print(Solution().fractionToDecimal(2, 3))
print(Solution().fractionToDecimal(4, 333))

