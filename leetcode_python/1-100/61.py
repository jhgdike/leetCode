# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        n, p, tail = 0, head, head
        while p:
            tail = p
            n += 1
            p = p.next
        if not n:
            return

        k %= n
        p = head
        while n - k > 1:
            p = p.next
            k += 1

        tail.next = head
        head = p.next
        p.next = None
        return head
