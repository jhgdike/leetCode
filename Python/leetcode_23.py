# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


from Queue import PriorityQueue
class Solution(object):
    def mergeKLists(self, lists):
        dummy = ListNode(None)
        curr = dummy
        q = PriorityQueue()
        for node in lists:
            if node:
                q.put((node.val,node))
        while q.qsize() > 0:
            curr.next = q.get()[1]
            curr = curr.next
            if curr.next:
                q.put((curr.next.val, curr.next))
        return dummy.next


from operator import attrgetter

class Solution1:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        sorted_list = []
        for head in lists:
            curr = head
            while curr is not None:
                sorted_list.append(curr)
                curr = curr.next

        sorted_list = sorted(sorted_list, key=attrgetter('val'))
        for i, node in enumerate(sorted_list):
            try:
                node.next = sorted_list[i + 1]
            except:
                node.next = None

        if sorted_list:
            return sorted_list[0]
        else:
            return None


"""time limit exceeded"""
class _Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        root = ListNode(0)
        if not lists:
            return root
        root.next = lists[0]
        for i in range(1, len(lists)):
            self.merge_two(root, lists[i])
        return root.next

    def merge_two(self, node, node1):
        while node.next and node1:
            if node1.val < node.next.val:
                tmp = node.next
                node.next = node1
                node1 = tmp
            node = node.next
        if node.next is None:
            node.next = node1



