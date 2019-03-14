# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        pos = 0
        for i in range(1, len(preorder)):
            if preorder[i] > preorder[0]:
                pos = i
                break
        pos = pos or len(preorder)
        root.left = self.bstFromPreorder(preorder[1:pos])
        root.right = self.bstFromPreorder(preorder[pos:])
        return root


print(Solution().bstFromPreorder([4,2]))
