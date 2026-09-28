"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda meeting: meeting.start)
        for x in range(1, len(intervals)):
            if intervals[x].start < intervals[x - 1].end:
                return False    
        return True