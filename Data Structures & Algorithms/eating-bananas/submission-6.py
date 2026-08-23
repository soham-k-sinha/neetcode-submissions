class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = max(piles)
        l, r = 1, max(piles)

        while l <= r:
            m = (l + r) // 2
            cond = sum([math.ceil(p / m) for p in piles]) <= h
            if cond:
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        return res
