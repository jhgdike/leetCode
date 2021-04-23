class Solution3(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        rol = [0] * n
        min_ = matrix[0][rol[0]]
        for _ in range(k):
            min_ = None
            min_index = 0
            for j in range(n):
                if rol[j] < n:
                    if min_ is None or matrix[j][rol[j]] < min_:
                        min_ = matrix[j][rol[j]]
                        min_index = j
            rol[min_index] += 1
        return min_

import heapq
class Solution2(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        heap = [(matrix[i][0], i, 0) for i in range(n)]
        min_ = None
        for _ in range(k):
            min_, row, num = heapq.heappop(heap)
            if num < n-1:
                heapq.heappush(heap, (matrix[row][num+1], row, num+1))
        return min_


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """

        def check(mid):
            i, j = n-1, 0
            sum_ = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    sum_ += i+1
                    j += 1
                else:
                    i -= 1
            return sum_ >= k
        n = len(matrix)
        l, r = matrix[0][0], matrix[n-1][n-1]
        while l < r:
            mid = (l+r) // 2
            if check(mid):
                r = mid
            else:
                l = mid+1
        return l


print(Solution().kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8))
print(Solution().kthSmallest([[-5]], 1))
print(Solution().kthSmallest([[0,0,0],[2,7,9],[7,8,11]],7))
print(Solution().kthSmallest([[-5]], 1))
