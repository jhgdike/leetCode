class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        if k == 1:
            return 1
        if n < 10:
            return k
        if 10 <= n < 20:
            if n - 8 >= k:
                return 8+k
            else:
                return k - 4