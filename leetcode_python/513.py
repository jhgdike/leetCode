"""
Find Bottom Left Tree Value
Given a binary tree, find the leftmost value in the last row of the tree.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        cur_level, next_level = [root], []
        while True:
            for node in cur_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if not next_level:
                break
            cur_level = next_level
            next_level = []
        return cur_level[0].val
