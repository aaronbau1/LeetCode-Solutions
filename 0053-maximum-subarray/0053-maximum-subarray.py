class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # brute - find all the subarrays and sum them then return the maximum sum O(n^3)
        # better - prefix sum and store sums - iterate through and find the local difference max
        # optimal - sliding window where you reset the window if the count drops below 0

        asum = 0
        result = float(-inf)
        for i in range(len(nums)):
            asum += nums[i]
            result = max(result, asum)
            if asum < 0:
                asum = 0
        return result