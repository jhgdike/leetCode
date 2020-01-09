# The guess API is already defined for you.
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num: int) -> int:
    if num == 6:
        return 0
    elif num > 6:
        return -1
    return 1


class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n
        while True:
            if l == r:
                return l
            mid = (l + r) // 2
            ret = guess(mid)
            if ret == 0:
                return mid
            if ret == 1:
                l = mid + 1
            else:
                r = mid - 1

    def _guessNumber(self, l, r):
        if l == r:
            return l
        mid = (l + r) // 2
        ret = guess(mid)
        if ret == 0:
            return mid
        if ret == 1:
            return self._guessNumber(mid + 1, r)
        else:
            return self._guessNumber(l, mid - 1)


print(Solution().guessNumber(11))
