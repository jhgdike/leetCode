def getSwap(S, B):  # 用于获取一个节点下可以扩展的所有节点
    for i, c in enumerate(S):  # 找到第一个不相等的字符的-位置-
        if c != B[i]: break
    T = list(S)
    for j in range(i + 1, len(S)):  # 获取所有的可扩展的子节点
        if S[j] == B[i]:  # 找到就交换
            T[i], T[j] = T[j], T[i]
            yield ''.join(T)  # 返回一个节点
            T[j], T[i] = T[i], T[j]  # 恢复当前环境，以便寻找下一个可扩展的节点


class Solution(object):
    # def kSimilarity(self, A, B):
    #
    #     queue, cnt = [A], {A: 0}  # 初始化队列，cnt用于记录当前结点已经走了多少步
    #     while queue:
    #         S = queue[0]  # 出队
    #         del queue[0]
    #         if S == B: return cnt[S]  # 结束
    #         for T in getSwap(S, B):  # 获取当前节点所有扩展子节点
    #             if T not in cnt:  # 如果没有出现过，则入队
    #                 cnt[T] = cnt[S] + 1
    #                 queue.append(T)

    def remove_same(self, A, B):
        a, b = [], []
        for i in range(len(A)):
            if A[i] != B[i]:
                a.append(A[i])
                b.append(B[i])
        return ''.join(a), ''.join(b)

    def find_swap(self, A, B):
        count = 0
        for i in range(len(A)):
            for j in range(i+1, len(B)):
                if A[i] != A[j] and (A[i] == B[j] and A[j] == B[i]):
                    B[i], B[j] = B[j], B[i]
                    count += 1
        return count, A, B

    def kSimilarity(self, A, B):
        count, a, b = self.find_swap(list(A), list(B))
        a, b = self.remove_same(a, b)
        queue, cnt = [a], {a: count}
        while queue:
            S = queue.pop()
            if S == b:
                return cnt[b]
            for i, c in enumerate(S):
                if c != b[i]:break
            T = list(S)
            for j in range(i + 1, len(S)):
                if S[j] == b[i]:
                    T[i], T[j] = T[j], T[i]
                    t = ''.join(T)
                    T[j], T[i] = T[i], T[j]
                    if t not in cnt:
                        cnt[t] = cnt[S] + 1
                        queue.append(T)
#
# A, B = "aabbccddee","cdacbeebad"
# # A = "abcdeabcdeabcdeabcde"
# # B = "aaaabbbbccccddddeeee"

#
print(Solution().kSimilarity("ab", "ba"))


def kSimilarity(self, A, B):
    def getSwap(S):  # 用于获取一个节点下可以扩展的所有节点
        for i, c in enumerate(S):  # 找到第一个不相等的字符的-位置-
            if c != B[i]: break
        T = list(S)
        for j in range(i + 1, len(S)):  # 获取所有的可扩展的子节点
            if S[j] == B[i]:  # 找到就交换
                T[i], T[j] = T[j], T[i]
                yield ''.join(T)  # 返回一个节点
                T[j], T[i] = T[i], T[j]  # 恢复当前环境，以便寻找下一个可扩展的节点

    queue, cnt = [A], {A: 0}  # 初始化队列，cnt用于记录当前结点已经走了多少步
    while queue:
        S = queue[0]  # 出队
        del queue[0]
        if S == B: return cnt[S]  # 结束
        for T in getSwap(S):  # 获取当前节点所有扩展子节点
            if T not in cnt:  # 如果没有出现过，则入队
                cnt[T] = cnt[S] + 1
                queue.append(T)
