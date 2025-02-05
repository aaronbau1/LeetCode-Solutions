class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # binary search to find target value, then spread left and right
        left = -1
        right = -1
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                left = mid
                right = mid
                break
        if left == right and left != -1:
            while left > 0 and nums[left] == nums[left-1]:
                left -= 1
            while right < len(nums) - 1 and nums[right] == nums[right+1]:
                right += 1
        return [left, right]