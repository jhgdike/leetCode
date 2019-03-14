# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.helper(root)

    def helper(self, root):
        if not root.left and not root.right:
            return root, root

        if not root.right:
            root.right = root.left
            root.left = None
        r_h, r_t = self.helper(root.right)

        if root.left:
            head, tail = self.helper(root.left)
            tail.right = root.right
            root.right = head
            root.left = None
        return root, r_t


from leetcode_python.helper import form_tree


Solution().flatten(form_tree([1,2]))
Solution().flatten(form_tree([1,2,5,3,4,None,6]))
