# coding: utf-8


class Solution(object):
    """
    两个列表交叉。本题必然交叉,必然有环
    References: https://segmentfault.com/a/1190000003817671
    """

    def findDuplicate(self, nums):
        slow = fast = finder = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                while finder != slow:
                    finder = nums[finder]
                    slow = nums[slow]
                return finder
