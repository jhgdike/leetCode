# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self._iterator = []
        self._lpush(root)

    def _lpush(self, root):
        if root:
            self._iterator.insert(0, root)
            self._lpush(root.left)

    def hasNext(self):
        """
        :rtype: bool
        """
        return self._iterator != []

    def next(self):
        """
        :rtype: int
        """
        res = self._iterator.pop(0)
        self._lpush(res.right)
        return res.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
