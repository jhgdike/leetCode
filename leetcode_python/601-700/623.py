# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def addOneRow(self, root, val, depth):
        """
        :type root: TreeNode
        :type val: int
        :type depth: int
        :rtype: TreeNode
        """
        if depth == 1:
            return TreeNode(val, left=root)
        queue = [root]
        while depth > 2:
            nexts = []
            for node in queue:
                if node.left: nexts.append(node.left)
                if node.right: nexts.append(node.right)
            queue = nexts
            depth -= 1
        for node in queue:
            node.left = TreeNode(val, left=node.left)
            node.right = TreeNode(val, right=node.right)
        return root
