class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[0])

        prev = intervals[0]
        count = 0

        for curr in intervals[1:]:
            # no overlap
            if prev[1] <= curr[0]:
                prev = curr

            # overlaps
        else:
            # prev is longer
                if prev[1] > curr[1]:
                    prev = curr

                # curr is longer, do nothing

                count += 1

        return count
