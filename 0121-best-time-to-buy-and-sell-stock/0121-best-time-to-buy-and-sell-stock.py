class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_sum = 0
        local_min = float(inf)
        for i in range(0, len(prices)):
            local_min = min(local_min, prices[i])
            max_sum = max(max_sum, prices[i] - local_min)
        return max_sum