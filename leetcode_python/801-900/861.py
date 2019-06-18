class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        for arr in A:
            if arr[0] == 0:
                for i in range(len(arr)):
                    arr[i] ^= 1
        for i in range(1, len(A[0])):
            count = 0
            for j in range(len(A)):
                count += A[j][i]
            if count <= (len(A) // 2):
                for j in range(len(A)):
                    A[j][i] ^= 1
        # print(A)
        return sum([int('0b' + ''.join(map(str, x)), base=2) for x in A])


A = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
print(Solution().matrixScore(A))
