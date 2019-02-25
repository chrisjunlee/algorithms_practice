# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # greedy algorithm 
    def eraseOverlapIntervals(self, intervals: 'List[Interval]') -> 'int':
        toss_count = 0

        if not intervals:
            return 0

        # important to specify sort by 2 keys
        intervals.sort(key = lambda x: (x.start, x.end))

        prev = intervals[0]

        for interval in intervals[1:]:
            if prev.end <= interval.start:
                # case 1: disjoint
                prev = interval
            elif prev.start < interval.start and prev.end > interval.end:
                # case 2: completely contained. keep current
                    prev = interval
                    toss_count += 1
            else:
                # case 3: overlapping. keep previous
                toss_count += 1

        return toss_count
