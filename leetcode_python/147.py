# Definition for singly-linked list.
from helper import ListNode, arr_to_list
import heapq

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        root = ListNode(None)
        root.next = head
        cur = head
        while cur.next:
            tmp = root
            while tmp.next.val < cur.next.val:
                tmp = tmp.next
            if tmp == cur:
                cur = cur.next
                continue
            nx = tmp.next
            tmp.next = cur.next
            cur.next = cur.next.next
            tmp.next.next = nx
        return root.next


Solution().insertionSortList(arr_to_list([5,4,3,2,1]))
