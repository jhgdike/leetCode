# Definition for a binary tree node.
from helper import form_tree

#
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    th = 0
    kth = None

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k = k
        self._search(root)
        return self.kth

    def _search(self, root):
        if not root:
            return
        self._search(root.left)
        if self.th == self.k:
            return
        self.th += 1
        self.kth = root.val
        self._search(root.right)


root = form_tree([2,1,6,None,None,4,7])
print(Solution().kthSmallest(root, 3))
