class Solution(object):
    def minOperations(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        if len(nums1) > 6 * len(nums2) or len(nums2) > 6 * len(nums1):
            return -1
        s1, s2 = sum(nums1), sum(nums2)
        if s1 == s2:
            return 0
        if s1 > s2:
            nums1, nums2 = nums2, nums1
        set1 = [0] * 7
        set2 = [0] * 7
        for i in nums1:
            set1[i] += 1
        for i in nums2:
            set2[i] += 1
        diff = abs(s1-s2)
        cnt = diff // 6
        diff %= 6
        if set1

