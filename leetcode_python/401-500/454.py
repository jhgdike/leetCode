import collections


class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        qa = collections.Counter(A)
        qb = collections.Counter(B)
        q1 = collections.defaultdict(int)
        for k, cnt in qa.items():
            for bk, bcnt in qb.items():
                q1[k + bk] += cnt * bcnt
        qc = collections.Counter(C)
        qd = collections.Counter(D)
        q2 = collections.defaultdict(int)
        for k, cnt in qc.items():
            for bk, bcnt in qd.items():
                q2[k + bk] += cnt * bcnt
        ans = 0
        for k, cnt in q1.items():
            for k2, cnt2 in q2.items():
                if k + k2 == 0:
                    ans += cnt * cnt2
        return ans


print(Solution().fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]))
