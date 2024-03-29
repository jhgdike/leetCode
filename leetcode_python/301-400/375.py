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


class Solution2:
    def getMoneyAmount(self, n):
        def find_max(l, r):
            if l >= r:
                return 0
            if l + 1 == r:
                return l
            if l + 2 == r:
                return l + 1
            mid = (l + r) * 2 // 3
            return max(find_max(l, mid - 1), find_max(mid + 1, r)) + mid

        return find_max(1, n)


class Solution3:
    def getMoneyAmount(self, n):
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        def cal_money(i, j):
            if i >= j:
                return 0
            elif i + 1 == j:
                return i
            elif i + 2 == j:
                return i + 1
            elif i + 3 == j:
                return 2 * i + 2
            elif i + 4 == j:
                return 2 * i + 4
            else:
                return dp[i][j]

        for i in range(n - 4, 0, -1):
            for j in range(i + 5, n + 1):
                dp[i][j] = min([max(cal_money(i, k - 1), cal_money(k + 1, j)) + k for k in range(i, j+1)])
                # dp[i][j] = min([cal_money(i, k - 1) + cal_money(k + 1, j) + k for k in range(i + 1, j)])
        return cal_money(1, n)


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


# print(guibing_sort([[1,4,6,7], [2,5,9,10], [3,11,28,39]]))
for i in range(6, 11):
    # print(Solution3().getMoneyAmount(i))
    print(Solution2().getMoneyAmount(i), Solution3().getMoneyAmount(i))
print(Solution2().getMoneyAmount(10))
