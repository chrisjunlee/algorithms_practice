# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def canAttendMeetings(self, intervals: 'List[Interval]') -> 'bool':
        end = 0

        for interval in sorted(intervals, key= lambda k: k.start):
            if interval.start < end:
                return False

            end = interval.end

        return True
