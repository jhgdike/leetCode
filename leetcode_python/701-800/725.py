# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        cur = head
        l = 0
        while cur:
            l += 1
            cur = cur.next
        n = l // k
        o = l - n*k
        ans = [None] * k
        cur = head
        for i in range(k):
            ans[i] = cur
            for _ in range(n-1):
                if not cur:
                    break
                cur = cur.next
            if n and o and cur:
                cur = cur.next
                o -= 1
            if not cur:
                break
            pre = cur
            cur = cur.next
            pre.next = None
        return ans


Solution().splitListToParts(ListNode(1, ListNode(2, ListNode(3))), 5)
