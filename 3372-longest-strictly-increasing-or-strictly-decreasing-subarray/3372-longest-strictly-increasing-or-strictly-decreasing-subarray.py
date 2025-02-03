class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        
        result = 1
        count = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                count += 1
                result = max(count, result)
            else:
                count = 1
        print(result)
        count = 1
        for i in range(len(nums)-1, 0, -1):
            if nums[i-1] > nums[i]:
                count += 1
                result = max(count, result)
            else:
                count = 1

        return result
