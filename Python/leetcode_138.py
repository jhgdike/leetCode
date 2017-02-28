"""
Title: Copy List with Random Pointer

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

Subscribe to see which companies asked this question.
"""


# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        cur = head
        while cur:
            new_node = RandomListNode(cur.label)
            new_node.next = cur.next
            cur.next = new_node

            cur = new_node.next

        res = RandomListNode(0)
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        cur = head
        new_cur = res
        while cur:
            new_cur.next = cur.next
            cur.next = new_cur.next.next
            new_cur = new_cur.next
            cur = cur.next
        return res.next
