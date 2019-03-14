# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        stack = [root]
        if not root:
            return res
        pos = 1
        while stack:
            tmp = stack
            stack = []
            cur = []
            for node in tmp:
                if pos:
                    cur.append(node.val)
                else:
                    cur.insert(0, node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            res.append(cur)
            pos ^= 1
        return res
