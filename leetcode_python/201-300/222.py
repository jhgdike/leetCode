# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        up, below = [root], []
        count = 1
        while True:
            for i, node in enumerate(up):
                if not node.left:
                    return count
                count += 1
                below.append(node.left)
                if not node.right:
                    return count
                count += 1
                below.append(node.right)
            up, below = below, []

    def faster(self, root):
        if not root:
            return 0
        left = right = root
        height = 0
        while (right):
            left = left.left
            right = right.right
            height += 1
        if left == None:
            return (1 << height) - 1
        else:
            return self.faster(root.left) + self.faster(root.right) + 1
