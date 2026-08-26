class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        heapq.heapify(minHeap)

        for i in nums:
            heapq.heappush(minHeap, i)
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        return minHeap[0]

        # O(n log k) time
        # O(k) space