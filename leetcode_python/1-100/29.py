class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if not divisor or (dividend == -2147483648 and divisor == -1):
            return 2147483648
        sign = -1 if (divisor < 0) ^ (dividend < 0) else 1
        dvd, dvs = abs(dividend), abs(divisor)
        res = 0
        while dvd >= dvs:
            tmp, mul = dvs, 1
            while dvd >= tmp << 1:
                tmp <<= 1
                mul <<= 1
            dvd -= tmp
            res += mul
        return sign * res
