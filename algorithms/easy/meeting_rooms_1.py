"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from typing import List


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        # Write your code here
        intervals.sort(key=lambda interval: interval.start)
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i-1].end:
                return False

        return True

intervals = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
assert(Solution().can_attend_meetings(intervals) == False)

intervals = [Interval(5, 8), Interval(9, 15)]
assert(Solution().can_attend_meetings(intervals))
