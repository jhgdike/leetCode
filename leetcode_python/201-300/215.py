import heapq


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        div = len(nums) // 2
        if div < k:
            k = len(nums) -k + 1
            comp = -1
        else:
            comp = 1
        heap = []
        for n in nums:
            if len(heap) < k:
                heapq.heappush(heap, comp*n)
            else:
                heapq.heappushpop(heap, comp*n)
        return comp * heap[0]

    def test(self):
        heapq.nlargest()


print(Solution().findKthLargest([3,2,1,5,6,4], 2))
print(Solution().findKthLargest([3,2,1,5,6,4], 5))
print(Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 4))

