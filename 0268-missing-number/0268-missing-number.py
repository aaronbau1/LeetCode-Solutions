class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = len(nums)
        for i in range(0, len(nums)):
            result = result ^ i ^ nums[i]
        return result