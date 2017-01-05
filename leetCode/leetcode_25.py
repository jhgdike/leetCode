# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        dummy = jump = ListNode(0)
        dummy.next = l = r = head

        while True:
            count = 0
            while r and count < k:  # use r to locate the range
                r = r.next
                count += 1
            if count == k:  # if size k satisfied, reverse the inner linked list
                pre, cur = r, l
                for _ in range(k):
                    cur.next, cur, pre = pre, cur.next, cur  # standard reversing
                jump.next, jump, l = pre, l, r  # connect two k-groups
            else:
                return dummy.next


class Solution2(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        curr = dummy = ListNode(None)
        stack = [None] * k
        curr.next = nt = head
        while nt:
            for i in range(k):
                stack[i] = nt
                if not nt:
                    break
                nt = nt.next
            else:
                for j in range(k):
                    curr.next = stack[k-j-1]
                    curr = curr.next
                if curr:
                    curr.next = nt

        return dummy.next
