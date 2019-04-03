# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        return self.helper(head, 1 << 63)

    def helper(self, head, upper):
        if not head or head.val >= upper:
            return head
        root = ListNode(None)
        root.next = head
        last = head
        cur = head.next
        move = False
        while cur:
            if cur.val > upper:
                break
            if cur.val == head.val:
                if cur == head.next:
                    last = cur
                    cur = cur.next
                    continue
                h_n = head.next
                head.next = cur
                last.next = cur.next
                cur.next = h_n
                head = cur
                move = True
            elif cur.val < head.val:
                r_n = root.next
                root.next = cur
                last.next = cur.next
                cur.next = r_n
                move = True
            else:
                last = cur
            cur = last.next
        if not move:
            head.next = self.helper(head.next, upper)
            return root.next
        root.next = self.helper(root.next, head.val)
        head.next = self.helper(head.next, upper)
        return root.next


from leetcode_python.helper import arr_to_list, list_to_arr

# node = arr_to_list([-84,142,41,-17,-71,170,186,183,-21,-76,76,10,29,81,112,-39,-6,-43,58,41,111,33,69,97,-38,82,-44,-7,99,135,42,150,149,-21,-30,164,153,92,180,-61,99,-81,147,109,34,98,14,178,105,5,43,46,40,-37,23,16,123,-53,34,192,-73,94,39,96,115,88,-31,-96,106,131,64,189,-91,-34,-56,-22,105,104,22,-31,-43,90,96,65,-85,184,85,90,118,152,-31,161,22,104,-85,160,120,-31,144,115])
# node = arr_to_list([-84,142,41,-17,-71,170,186,183,-21,-76,76,10,29,81,112,-39,-6,-43,58,41,111,33,69,97,-38,82,-44,-7,99,135,42,150,149,-21,-30,164,153,92,180,-61,99,-81,147,109,34,98,14,178,105,5,43,46,40,-37,23,16,123,-53,34,192,-73,94,39,96,115,88,-31,-96,106,131,64,189,-91,-34,-56,-22,105,104,22,-31,-43,90,96,65,-85,184,85,90,118,152,-31,161,22,104,-85,160,120,-31,144,115])
# node = arr_to_list([9,10,9,3,2,4,6,4,7,3,2,9,9,9,9,10,3,4,5,6,8,7,6,5,4,3,2,1,2,3,4,5,6,7,8,9])

node = [0, 2, 5, 8, 3, 4, 9, 1, 7, 6]
print(list_to_arr(Solution().sortList(arr_to_list(node))))

# import random
# node = list(range(10))
# for i in range(10):
#     print('******')
#     random.shuffle(node)
#     print(node)
#     res = list_to_arr(Solution().sortList(arr_to_list(node)))
#     print(res)
#     print(res == sorted(res))
