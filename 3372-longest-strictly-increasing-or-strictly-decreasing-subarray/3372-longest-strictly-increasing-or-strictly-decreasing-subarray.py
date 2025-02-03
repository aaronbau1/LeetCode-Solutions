class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        
        result = 1
        right_count = 1
        left_count = 1
        i = 1
        while i < len(nums):
            # increasing
            if nums[i] > nums[i-1]:
                right_count += 1
                result = max(right_count, result)
            else:
                right_count = 1

            if nums[len(nums)-i-1] > nums[len(nums)-i]:
                left_count += 1
                result = max(left_count, result)
            else:
                left_count = 1
            i += 1
        return result