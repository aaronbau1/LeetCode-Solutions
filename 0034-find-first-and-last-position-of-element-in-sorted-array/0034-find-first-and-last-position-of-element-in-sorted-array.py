class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums) - 1
        floor = -1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                if nums[mid] == target:
                    floor = mid
                high = mid - 1
            else:
                low = mid + 1
        
        if floor == -1:
            return[-1, -1]
        
        low = 0
        high = len(nums) - 1
        ceil = -1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] <= target:
                if nums[mid] == target:
                    ceil = mid
                low = mid + 1
            else:
                high = mid - 1
        return [floor, ceil]