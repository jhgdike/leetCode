from typing import List
import heapq


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
        nums1 = nums1[:k]
        nums2 = nums2[:k]
        res = []
        last = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if i > 0 and len(res) >= k and nums1[i] + nums2[j] > last:
                    break
                heapq.heappush(res, (nums1[i] + nums2[j], (nums1[i], nums2[j])))
            last = res[-1][0]
        ans = []
        while res:
            ans.append(heapq.heappop(res)[1])
        return ans[:k]


print(Solution().kSmallestPairs([1,1,2],[1,2,3],2))