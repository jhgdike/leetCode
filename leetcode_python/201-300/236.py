# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def dfs(node):
            if not node:
                return
            eq = node.val == p.val or node.val == q.val

            l = dfs(node.left)
            if eq and l:
                return node
            r = dfs(node.right)
            if eq and r:
                return node
            if l and r:
                return node
            return eq and node or l or r
        return dfs(root)

    def test(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        def dfs(node):
            if not node:
                return
            l = dfs(node.left)
            r = dfs(node.right)
            if l and r:
                return node
            if node.val == p.val or node.val == q.val:
                return node
            return l or r

        return dfs(root)


from leetcode_python.helper import form_tree
print(Solution().test(form_tree([3,5,1,6,2,0,8,None,None,7,4]), TreeNode(5), TreeNode(1)).val)
