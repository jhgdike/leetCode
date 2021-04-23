# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

def __gt__(self, other):
    return self.val > other.val

def __lt__(self, other):
    return self.val < other.val

def __eq__(self, other):
    return self.val == other.val

def __ge__(self, other):
    return self.val >= other.val

def __le__(self, other):
    return self.val <= other.val


from operator import attrgetter
import heapq


class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        heap = []
        for curr in lists:
            if curr:
                heapq.heappush(heap, curr)
        head = pre = None
        while heap:
            cur = heap[0]
            if not head:
                pre = head = cur
            else:
                pre.next = cur
                pre = cur
            cur = cur.next
            if cur:
                heapq.heapreplace(heap, cur)
            else:
                heapq.heappop(heap)

        return head


def arr_to_list(nums):
    if not nums:
        return
    origin = ListNode(nums[0])
    l = origin
    for num in nums[1:]:
        l.next = ListNode(num)
        l = l.next
    return origin


s = Solution()
s.mergeKLists([
    arr_to_list([1, 4, 5]),
    arr_to_list([1, 3, 4]),
    arr_to_list([2, 6])])

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
