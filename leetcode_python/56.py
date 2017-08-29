# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
from operator import attrgetter

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=attrgetter('start'))
        res = []
        if not intervals:
            return res
        res.append(intervals[0])
        for i in range(1, len(intervals)):
            if res[-1].end < intervals[i].start:
                res.append(intervals[i])
            elif res[-1].end < intervals[i].end:
                res[-1].end = intervals[i].end
        return res
