class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        确保lo->lo+1 , hi-1<-hi这两个方向是上升趋势，必然在lo和hi之间存在峰
        """
        if len(nums) == 1 or nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums) - 1
        l, r = -1, len(nums)
        while True:
            m = (l + r) // 2
            if r - l == 2:
                return l + 1
            if nums[m] < nums[m+1]:
                l = m
            else:
                r = m + 1




"""
输入: nums = [1,2,1,3,5,6,4]
输出: 1 或 5 
解释: 你的函数可以返回索引 1，其峰值元素为 2；
     或者返回索引 5， 其峰值元素为 6。

输入: nums = [1,2,3,1]
输出: 2
解释: 3 是峰值元素，你的函数应该返回其索引 2。
"""
