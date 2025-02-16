class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        result = len(nums)

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        return result