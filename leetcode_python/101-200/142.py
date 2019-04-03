# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast, slow = head, head
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                start = head
                while start != slow:
                    start, slow = start.next, slow.next
                return start
