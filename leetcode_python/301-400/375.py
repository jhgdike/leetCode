# The guess API is already defined for you.
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num: int, n) -> int:
    if num == n:
        return 0
    elif num > n:
        return -1
    return 1


class Solution:
    def getMoneyAmount(self, n: int) -> int:
        l = 1
        r = n
        ans = 0
        while True:
            if l == r:
                return ans
            if l + 1 == r:
                return ans + l
            if l + 2 == r:
                return ans + l + 1
            mid = (l + r) * 2 // 3
            ret = guess(mid, n)
            if ret == 0:
                return ans
            ans += mid
            if ret == 1:
                l = mid + 1
            else:
                r = mid - 1


class Node(object):
    data = None
    left = None
    right = None

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def print_tree_by_layer(root):
    cur_layer = [root]
    next_layer = []
    while cur_layer:
        for node in cur_layer:
            print(node.data)
            if node.left:
                next_layer.append(node.left)
            if node.right:
                next_layer.append(node.right)
        cur_layer = next_layer
        next_layer = []


def test():
    root = Node(1, Node(2, Node(3)), Node(4))
    print_tree_by_layer(root)


def guibing_sort(lists):
  ans = []
  while lists:
    cur_min = lists[0][0]
    min_index = 0
    for i, l in enumerate(lists):
      if cur_min > l[0]:
        cur_min = l[0]
        min_index = i
    ans.append(lists[min_index][0])
    lists[min_index].pop(0)
    if not lists[min_index]:
      lists.pop(min_index)
  return ans

print(guibing_sort([[1,4,6,7], [2,5,9,10], [3,11,28,39]]))