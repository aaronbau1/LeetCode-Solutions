class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Brute
        # Move all into a hash array, then check to see which value only has 1 O(n) O(n)
        # Optimal
        # Use XOR operator and iterate through O(n) since x^x = 0
        result = 0
        for i in range(0,len(nums)):
            result = result ^ nums[i]
        return result