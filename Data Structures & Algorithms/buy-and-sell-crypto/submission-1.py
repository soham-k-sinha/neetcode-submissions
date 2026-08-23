class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # A profit happens when you buy at a lower price than you sell
        # We can use a 2 pointer approach because we can't sell a stock at an earlier time than buying it, starting l at 0 and r at 1 (prices.length >= 1, so no need to worry about empty or 1 element list)
        # If we buy at a higher price than sell prices[l] > prices[r] we should increment both l and r because we don't want a loss (0 is the max initially). 
        # If we do get a profit then let's keep looking for a bigger profit.

        # Basically if an element is lower than it's preceeding element, it's a much better buying day than the previous day because we confirm higher profits (because the rest of the selling days are the same for both days)

        max_profit = 0
        l, r = 0, 1
        while r < len(prices):
            max_profit = max(max_profit, prices[r] - prices[l])
            if prices[l] >= prices[r]:
                # Skip all the elements in the middle and move l to r and increment r by 1 to check the next element
                l = r
                r += 1
            else:
                r += 1
        return max_profit