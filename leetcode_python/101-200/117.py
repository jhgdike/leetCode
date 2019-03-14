"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return
        node = root
        while node:
            prev = None
            head = None
            while node:
                if node.left:
                    if not prev:
                        head = node.left
                    else:
                        prev.next = node.left
                    prev = node.left
                if node.right:
                    if not prev:
                        head = node.right
                    else:
                        prev.next = node.right
                    prev = node.right
                node = node.next
            node = head
        return root
