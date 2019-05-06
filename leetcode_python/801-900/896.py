class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        l = r = True
        for i in range(len(A) - 1):
            if A[i] > A[i+1]:
                if not r:
                    return False
                l = False
            elif A[i] < A[i+1]:
                if not l:
                    return False
                r = False

        return True
