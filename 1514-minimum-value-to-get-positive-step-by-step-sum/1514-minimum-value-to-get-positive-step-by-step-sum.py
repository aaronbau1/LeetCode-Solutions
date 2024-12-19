class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        # Make sure the sum never goes below 1
        sum = 0
        min = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum <= min: min = sum
        return 1 - min