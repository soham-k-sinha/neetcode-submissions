class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Heapify - O(n) - Min heap
        # Pop n-k times to get the kth largest element

        heapq.heapify(nums)
        res = 0
        val = len(nums) - k
        while val >= 0:
            res = heapq.heappop(nums)
            val -= 1
        
        return res