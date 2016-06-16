# coding: utf-8

"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution(object):

    def rightSideView(self, root):
        res = []
        if root:
            next_level = [root]
            while next_level:
                res += next_level[-1].val
                next_level = [kid for node in next_level for kid in (node.left, node.right) if kid]
        return res
