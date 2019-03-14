# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.helper(root)

    def helper(self, root, upper=(1 << 63) - 1, lower=-1 << 63):
        if root:
            if not lower < root.val < upper:
                return False
            return self.helper(root.left, root.val, lower) and self.helper(root.right, upper, root.val)
        return True
        #
        # if not root.left:
        #     return root.val < root.right.val < upper and self.helper(root.right, lower=root.val, upper=upper)
        # if not root.right:
        #     return root.val > root.left.val > lower and self.helper(root.left, upper=root.val, lower=lower)
        # return lower < root.left.val < root.val < root.right.val < upper and \
        #        self.helper(root.left, upper=root.val, lower=lower) and self.helper(root.right, lower=root.val,
        #                                                                            upper=upper)

        # return self.valid_tree(root, root)


from leetcode_python.helper import form_tree

test_case = [
    ([3, 1, 5, 0, 2, 4, 6, None, None, None, 3], False),
    ([3, None, 30, 10, None, None, 15, None, 45], False)
]
for i, v in test_case:
    print(Solution().isValidBST(form_tree(i)), v)
