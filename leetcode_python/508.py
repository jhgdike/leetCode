"""
Most Frequent Subtree Sum
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.max_count = 0
        self.count_dict = {}
        self.count_subtree(root)

    def count_subtree(self, root):
        if not root:
            return 0
        res = self.count_subtree(root.left) + self.count_subtree(root.right) + self.val
        self.count_dict.setdefault(res, 0)
        self.count_dict[res] += 1