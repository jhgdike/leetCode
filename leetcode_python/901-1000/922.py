class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        s, d = 1, 0
        while s < len(A):
            while s < len(A) and A[s] & 1:
                s += 2
            while d < len(A) and not (A[d] & 1):
                d += 2
            if s < len(A):
                A[s], A[d] = A[d], A[s]
        return A
