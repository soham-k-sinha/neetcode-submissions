class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [[math.sqrt(x**2 + y**2), i] for i, (x, y) in enumerate(points)]
        heapq.heapify(distances)

        closest = []
        for i in range(k):
            closest.append(points[heapq.heappop(distances)[1]])
        
        return closest