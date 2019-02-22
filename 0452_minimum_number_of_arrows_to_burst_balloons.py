class Solution:
    def findMinArrowShots(self, points: 'List[List[int]]') -> 'int':
        if not points:
            return 0

        points.sort(key = lambda x: x[0])
        res = [points[0]]

        for point in points[1:]:
            if point[0] <= res[-1][1]:
                res[-1][1] = min(res[-1][1], point[1])
            else:
                res.append(point)

        return len(res)
