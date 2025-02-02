class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = float("-inf")
        preprod = 1
        suffprod = 1
        for i in range(len(nums)):
            preprod *= nums[i]
            suffprod *= nums[len(nums)-i-1]

            result = max(result, max(preprod, suffprod))
            if preprod == 0:
                preprod = 1
            if suffprod == 0:
                suffprod = 1
        return result