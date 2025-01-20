class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_index = 0
        n = len(nums)
        while zero_index < n and nums[zero_index] != 0:
            zero_index += 1
        
        for i in range(zero_index, n):
            if nums[i] != 0:
                nums[i], nums[zero_index] = nums[zero_index], nums[i]
                zero_index += 1
            