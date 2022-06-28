class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        def helper(node):
            pre = node
            while node:
                if node.child:
                    nx = node.next
                    node.next = node.child
                    node.child.prev = node
                    ch = helper(node.child)
                    node.child = None
                    ch.next = nx
                    if nx:
                        nx.prev = ch
                pre = node
                node = node.next
            return pre
        helper(head)
        return head


arr = [1,2,3,4,5,6,7,8,9,10,11,12]

nodes = [Node(val, None, None, None) for val in arr]
head = nodes[0]
head.next = nodes[1]
for i in range(1, 11):
    nodes[i].prev = nodes[i-1]
    nodes[i].next = nodes[i+1]
nodes[11].prev=nodes[10]

nodes[5].next=None
nodes[6].prev=None
nodes[9].next=None
nodes[10].prev=None

nodes[2].child=nodes[6]
nodes[7].child=nodes[10]

Solution().flatten(head)
while head:
    print(head.val, head.prev and head.prev.val, head.next and head.next.val, head.child)
    head=head.next
