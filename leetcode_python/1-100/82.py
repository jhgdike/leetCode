# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        root = ListNode(None)
        root.next = head
        cur = root
        while cur.next:
            head = cur.next
            end = cur.next.next
            flag = False
            while end and head.val == end.val:
                flag = True
                end = end.next
            if flag:
                cur.next = end
            else:
                cur = cur.next
        return root.next


from leetcode_python.helper import arr_to_list, list_to_arr

print(list_to_arr(Solution().deleteDuplicates(arr_to_list([1,2,3,3,4,4,5]))))
