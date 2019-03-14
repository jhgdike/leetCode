# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[Interval]
        :type B: List[Interval]
        :rtype: List[Interval]
        """
        res = []
        cur_a, cur = 0, 0

        while cur_a < len(A) and cur < len(B):
            if A[cur_a].end < B[cur].start:
                cur_a += 1
            elif B[cur].end < A[cur_a].start:
                cur += 1
            elif A[cur_a].end < B[cur].end:
                if A[cur_a].start > B[cur].start:
                    res.append(Interval(A[cur_a].start, A[cur_a].end))
                else:
                    res.append(Interval(B[cur_a].start, A[cur_a].end))
                cur_a += 1
            else:
                if A[cur_a].start > B[cur].start:
                    res.append(Interval(A[cur_a].start, B[cur].end))
                else:
                    res.append(Interval(B[cur_a].start, B[cur].end))
                cur += 1

        return res


print(Solution().intervalIntersection([Interval(*x) for x in ([0,2],[5,10],[13,23],[24,25])],
[Interval(*x) for x in ([1,5],[8,12],[15,24],[25,26])]))
