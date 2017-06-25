class Solution:  #: 44ms
    def rotate(self, A):
        A[:] = zip(*A[::-1])


class Solution2:  #: 52ms
    def rotate(self, A):
        n = len(A)
        for i in range(n/2):
            for j in range(n-n/2):
                A[i][j], A[~j][i], A[~i][~j], A[j][~i] = \
                         A[~j][i], A[~i][~j], A[j][~i], A[i][j]

class Solution3:  #: 40ms
    def rotate(self, A):
        A.reverse()
        for i in range(len(A)):
            for j in range(i):
                A[i][j], A[j][i] = A[j][i], A[i][j]


class Solution4:  #: 48ms
    def rotate(self, A):
        n = len(A)
        for i in range(n):
            for j in range(i):
                A[i][j], A[j][i] = A[j][i], A[i][j]
        for row in A:
            for j in range(n/2):
                row[j], row[~j] = row[~j], row[j]


class Solution5:  #: 40ms
    def rotate(self, A):
        n = len(A)
        for i in range(n/2):
            for j in range(n-n/2):
                for _ in '123':
                    A[i][j], A[~j][i], i, j = A[~j][i], A[i][j], ~j, ~i
                i = ~j
