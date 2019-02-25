# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


import heapq

class Solution:
    def minMeetingRooms(self, intervals: 'List[Interval]') -> 'int':
        if not intervals: 
            return 0

        rooms = []

        intervals.sort(key = lambda k: k.start)

        heapq.heappush(rooms, intervals[0].end)

        for interval in intervals[1:]:

            if interval.start < rooms[0]:
                # overlap, create new room
                heapq.heappush(rooms, interval.end)
            else:
                # no overlap, release room
                heapq.heappop(rooms)
                heapq.heappush(rooms, interval.end)

        return len(rooms)



