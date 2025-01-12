class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_day = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            local_p = prices[i] - buy_day
            profit = max(local_p, profit)
            if prices[i] < buy_day:
                buy_day = prices[i]
        return profit