# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.res = []
        if not root:
            return self.res
        self.helper(root, [], sum)
        return self.res

    def helper(self, root, pre, sum):
        if not root:
            return
        if not root.cur:
            root.cur = pre + [root.val]
        sum -= root.val
        if not root.left and not root.right:
            if sum == 0:
                self.res.append(root.cur)
        else:
            self.helper(root.left, root.cur, sum)
            self.helper(root.right, root.cur, sum)


# [5,4,8,11,null,13,4,7,2,null,null,5,1]
# 22
# [[5,4,11,2],[5,8,4,5]]


class Solution2:
    def __init__(self):
        self.res = []
        self.track = []

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.dfs(sum, root)
        return self.res

    def dfs(self, Sum, Node):
        if Node is None:
            return
        self.track.append(Node.val)
        Sum = Sum - Node.val
        if Sum == 0 and Node.left is None and Node.right is None:
            self.res.append(self.track[:])
        self.dfs(Sum, Node.left)
        self.dfs(Sum, Node.right)
        self.track.pop()