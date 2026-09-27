class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestProfit = 0
        minPrice = prices[0]
        for x in range(1, len(prices)):
            bestProfit = max(bestProfit, prices[x] - minPrice)
            minPrice = min(minPrice, prices[x])
        return bestProfit
