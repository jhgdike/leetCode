# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def findDeeps(root, level):
            if not root or (not root.left and not root.right):
                return level
            return max(findDeeps(root.left, level+1), findDeeps(root.right, level+1))
        deep = findDeeps(root, 0)
        # return deep
        if not deep:
            return root

        def findLeave(root, level):
            if not root:
                return
            if level == deep:
                return root
            l = findLeave(root.left, level + 1)
            r = findLeave(root.right, level + 1)
            if l and r:
                return root
            return l or r

        return findLeave(root, 0)

from leetcode_python.helper import form_tree
print(Solution().lcaDeepestLeaves(form_tree([3,5,1,6,2,0,8,None,None,7,4])).val)
print(Solution().lcaDeepestLeaves(form_tree([0,1,3,None,2])).val)

