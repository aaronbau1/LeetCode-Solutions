class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # find lower bound and find upper bound
        low = 0
        high = len(nums) - 1
        first = -1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                first = mid
                high = mid - 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        
        if first == -1:
            return [-1, -1]

        # find upper bound
        low = 0
        high = len(nums) - 1
        last = -1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                last = mid
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return [first, last]