class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # If profit <= 0 move both left = right and right ++
        # If profit > 0 let left be the same and right ++
        max_profit = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[r] - prices[l] <= 0:
                l = r
                r += 1
            else:
                max_profit = max(max_profit, prices[r] - prices[l])
                r += 1
        return max_profit
            
        