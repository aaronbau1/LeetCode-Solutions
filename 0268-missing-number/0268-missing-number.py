class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # [0,1] = 2 ^ 0 ^ 1 ^ 0 ^ 1
        val = len(nums)
        for i in range(len(nums)):
            val = val ^ nums[i] ^ i
        return val
