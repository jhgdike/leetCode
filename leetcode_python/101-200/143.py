# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        fast, slow = head, head
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        sec = slow.next
        slow.next = None

        sec_next = None
        while sec:
            cur = sec.next
            sec.next = sec_next
            sec_next = sec
            sec = cur
        tail = sec_next
        cur = head
        while cur and tail:
            cur_next = cur.next
            cur.next = tail
            tail_next = tail.next
            tail.next = cur_next
            cur = cur_next
            tail = tail_next
        if tail:
            cur.next = tail

