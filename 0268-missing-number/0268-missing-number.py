class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Brute
        # iterate through 0-n and see if value is included in the list using "val in nums" O(n^2)
        # Optimal
        # Use XOR operator O(n) 
        result = len(nums)
        # 3
        # O ^ 1 ^ 2
        # 3 ^ 0 ^ 1
        for i in range(0, len(nums)):
            result ^= i ^ nums[i]
        return result