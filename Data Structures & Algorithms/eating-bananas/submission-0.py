class Solution:
    import math
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if sum(piles) <= h:
            return 1
        min_rate = max(piles)

        l, r = 1, max(piles)
        while l <= r:
            m = (l+r) // 2
            cond = sum([math.ceil(p / m) for p in piles]) <= h
            if cond:
                r = m - 1
                min_rate = min(min_rate, m)
            else:
                l = m + 1
        
        return min_rate