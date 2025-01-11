class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = 0
        for i in range(len(nums)):
            total += nums[i]
        
        index = 0
        right = total
        left = 0
        while (index < len(nums)):
            left += nums[index]
            if left == right:
                return index
            right -= nums[index]
            index += 1
        return -1
        