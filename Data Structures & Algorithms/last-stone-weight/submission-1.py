class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Make a max heap - O(n) time
        stones = [-n for n in stones]
        heapq.heapify(stones) 

        # O(n) time
        while len(stones) > 1:
            # Pop 1 stone and peek other - O(log n) + O(1)
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)

            if stone1 == stone2:
                continue
            else:
                heapq.heappush(stones, stone1 - stone2)
        
        return -stones[0] if stones else 0