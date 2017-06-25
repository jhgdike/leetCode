"""
Teemo Attacking
"""

class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if not timeSeries:
            return 0
        pos_time = 0
        for i in range(1, len(timeSeries)):
            interval = timeSeries[i] - timeSeries[i-1]
            if interval > duration:
                pos_time += duration
            else:
                pos_time += interval
        return pos_time + duration
