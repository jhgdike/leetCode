"""
Find Largest Value in Each Tree Row


"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        cur_level, next_level = [root], []
        res, max_l = [], None
        while True:
            max_l = None
            for node in cur_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                if max_l is None:
                    max_l = node.val
                elif max_l < node.val:
                    max_l = node.val
            res.append(max_l)
            if not next_level:
                break
            cur_level = next_level
            next_level = []
        return res
