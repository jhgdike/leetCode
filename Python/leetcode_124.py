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
        self.max_sum = None
        if not root:
            return 0
        self.recursion(root)
        return self.max_sum

    def recursion(self, root):
        if not root:
            return
        branch = self.recursion(root.left), self.recursion(root.right)
        arg = [x for x in branch if x is not None]
        if not arg:
            m = root.val
        else:
            m = max(max(arg) + root.val, root.val)

        if not self.max_sum:
            self.max_sum = root.val

        s_m = sum(arg) + root.val
        arg.extend([m, s_m])
        self.max_sum = max(m, s_m, self.max_sum)

        return m if m > 0 else None
