class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxEarn = 0
        if len(prices) < 2:
            return 0
        
        while r < len(prices):
            left, right = prices[l], prices[r]
            if left < right:
                maxEarn = max(maxEarn, right - left)
            else:
                l = r
            r += 1

        return maxEarn

