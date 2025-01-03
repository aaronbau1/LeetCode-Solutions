class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = 0
        local_min = prices[0]

        for i in range(1, len(prices)):
            local_min = min(prices[i], local_min)
            diff = max(diff, prices[i] - local_min)
        return diff