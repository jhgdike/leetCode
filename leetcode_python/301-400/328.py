# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        odd = even = even_head = None
        cur = head
        while cur:
            if odd:
                odd.next = cur
            odd = cur
            if cur.next:
                if not even:
                    even_head = even = cur.next
                else:
                    even.next = cur.next
                    even = even.next
                cur = cur.next.next
            else:
                break
        odd.next = even_head
        if even:
            even.next = None
        return head
