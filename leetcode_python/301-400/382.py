# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random
class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head


    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        cur = self.head
        total = 1
        val = self.head.val
        while cur.next:
            total += 1
            if random.randint(1, total) == 1:
                val = cur.next.val
            cur = cur.next
        return val





# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()