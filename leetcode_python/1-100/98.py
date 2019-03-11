# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        return self.valid_tree(root, root)

    def valid_tree(self, node, root):
        if not node:
            return True
        if (node.left and node.left.val >= node.val) or (
            node.right and node.right.val <= node.val):
            return False
        return self.search(root, node.val) and self.valid_tree(node.left,
                                                               root) and self.valid_tree(
            node.right, root)

    def search(self, root, val):
        if not root:
            return False
        if val > root.val:
            self.search(root.right, val)
        elif val < root.val:
            self.search(root.left, val)
        else:
            return True
