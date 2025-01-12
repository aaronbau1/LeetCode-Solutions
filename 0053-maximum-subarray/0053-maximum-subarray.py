class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # brute find all subarrays and calculate sums
        # better: prefix sum and calculate greatest value from the hashmap
        # optimal: two pointers and start over when it is lower than zero
        local_sum = 0
        max_sum = float("-inf")

        for i in range(len(nums)):
            local_sum += nums[i]
            max_sum = max(max_sum, local_sum)
            if local_sum < 0:
                local_sum = 0
        return max_sum

            

