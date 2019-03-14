# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def insertIntoMaxTree(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return TreeNode(val)
        if val > root.val:
            val_node = TreeNode(val)
            val_node.left = root
            return val_node
        # if not root.right or root.right.val < val:
        #     right = root.right
        #     root.right = TreeNode(val)
        #     root.right.right = right
        #     return root
        root.right = self.insertIntoMaxTree(root.right, val)
        return root

