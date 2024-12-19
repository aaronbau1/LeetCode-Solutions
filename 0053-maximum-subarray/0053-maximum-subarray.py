class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Brute: Calculate sums for all subarrays possible
        # Better 
        # Optimal: Calculate sum at each point and then calculate the greatest pos jump
        
        psum = 0
        max_sum = float(-inf)
        for i in range(len(nums)):
            psum += nums[i]
            max_sum = max(max_sum, psum)
            if psum < 0:
                psum = 0
        return max_sum