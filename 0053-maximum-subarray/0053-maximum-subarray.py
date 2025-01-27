class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = float("-inf")
        psum = 0
        for i in range(len(nums)):
            psum += nums[i]
            total = max(psum, total)

            if psum < 0:
                psum = 0
        return total