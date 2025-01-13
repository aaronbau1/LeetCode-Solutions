class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_index = 0
        while nums[zero_index] != 0:
            zero_index += 1
            if zero_index >= len(nums) - 1:
                return
        
        for i in range(zero_index, len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero_index] = nums[zero_index], nums[i]
                zero_index += 1
        
