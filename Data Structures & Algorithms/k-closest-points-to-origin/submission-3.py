class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [[math.sqrt(x**2 + y**2), i] for i, (x, y) in enumerate(points)]
        heap = []
        heapq.heapify(heap)

        # O(n)
        for i in distances:
            # O(log k)
            heapq.heappush(heap, [-i[0], i[1]])

            # O(log k)
            if len(heap) > k:
                heapq.heappop(heap)

        # loop was O(nlogk)
        return [points[i[1]] for i in heap]