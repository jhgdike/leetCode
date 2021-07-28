from leetcode_python.helper import form_tree


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        if k == 0:
            return [target]
        m = dict()
        def dfs(node):
            if not node:
                return
            if node.left:
                m.setdefault(node.val, set()).add(node.left.val)
                m.setdefault(node.left.val, set()).add(node.val)
                dfs(node.left)
            if node.right:
                m.setdefault(node.val, set()).add(node.right.val)
                m.setdefault(node.right.val, set()).add(node.val)
                dfs(node.right)
        dfs(root)
        ans = m.get(target)
        if not ans:
            return []
        last = {target}
        while k > 1:
            nt = set()
            for item in ans:
                nt |= m.get(item, set())
            nt -= last
            last = ans
            ans = nt
            k -= 1
        print(m)
        return list(ans)


root = form_tree([3,5,1,6,2,0,8,None,None,7,4])
print(Solution().distanceK(root, 5, 2))
root = form_tree([0,1,2,None,None,3])
print(Solution().distanceK(root, 3, 3))
root = form_tree([0,1,None,None,2,None,3,None,4])
print(Solution().distanceK(root, 3, 0))
