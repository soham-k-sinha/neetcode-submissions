class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)

        # O(n)
        for i, l in enumerate(points):
            distance = math.sqrt(l[0]**2 + l[1]**2)
            # O(log k)
            heapq.heappush(heap, [-distance, i])

            # O(log k)
            if len(heap) > k:
                heapq.heappop(heap)

        # loop was O(nlogk)
        return [points[i[1]] for i in heap]
        # O(nlogk) time and O(k) space