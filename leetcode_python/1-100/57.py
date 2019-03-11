# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals or (
                        newInterval.start <= intervals[0].start and
                        newInterval.end >= intervals[-1].end):
            return [newInterval]
        if newInterval.end < intervals[0].start:
            intervals.insert(0, newInterval)
            return intervals
        if newInterval.start > intervals[-1].end:
            intervals.append(newInterval)
            return intervals

        start = end = None
        for i in range(len(intervals)):
            if newInterval.start > intervals[i].start:
                if newInterval.start <= intervals[i].end:
                    newInterval.start = intervals[i].start
                    start = i
                else:
                    start = i + 1
            if not end and newInterval.end < intervals[i].end:
                if newInterval.end >= intervals[i].start:
                    end = i + 1
                    newInterval.end = intervals[i].end
                else:
                    end = i # end is the first place where
            if start is not None and end is not None:
                break

        if start is None:
            return [newInterval] + intervals[end:]
        if end is None:
            return intervals[:start] + [newInterval]
        else:
            return intervals[:start] + [newInterval] + intervals[end:]

print(Solution().insert([Interval(1,3),Interval(6,9)], Interval(2,5)))


from operator import attrgetter

class Solution2(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        intervals.append(newInterval)
        return self.merge(intervals)

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
