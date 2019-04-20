import heapq

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return sorted(points, key=lambda p: p[0]**2 + p[1]**2)[:K]

    def kClosest_heap(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []

        for point in points:
            dist = dist_sqr(point)

            if len(heap) < K:
                heapq.heappush(heap, (-dist, point))
            else:
                if dist < abs(heap[0][0]):
                    heapq.heappushpop(heap, (-dist, point))

        res = []
        for x in range(min(K, len(heap))):
            res.append(heapq.heappop(heap)[1])

        return res


    def kClosest_bf(self, points: List[List[int]], K: int) -> List[List[int]]:
        dist_points = [(dist_sqr(point), point) for point in points]
        dist_points.sort()

        return [point for (dist, point) in dist_points[:K]]

def dist_sqr(point):
    return point[0]**2 + point[1]**2
