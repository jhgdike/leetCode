class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A.sort()
        i = 0
        while K > 0 and i < len(A) and A[i] < 0:
            K -= 1
            A[i] = -A[i]
            i += 1
        if K == 0:
            return sum(A)
        if i >= len(A):
            i -= 1
        if K & 1 == 0:
            return sum(A)
        sm = min(A[i], A[i-1])
        return sum(A) - (2 * sm)


print(Solution().largestSumAfterKNegations([2,-3,-1,5,-4], 2))
