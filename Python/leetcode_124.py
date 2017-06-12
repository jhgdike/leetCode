# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.max_sum = root.val
        self.recursion(root)
        return self.max_sum

    def recursion(self, root):
        if not root:
            return 0
        l, r = self.recursion(root.left), self.recursion(root.right)
        m = max(max(l, r) + root.val, root.val)

        self.max_sum = max(m, l + r + root.val, self.max_sum)
        return m if m > 0 else 0
