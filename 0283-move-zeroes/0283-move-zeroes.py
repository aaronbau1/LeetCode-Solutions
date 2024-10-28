class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_index = 0
        for i in range(len(nums)):
            if i == 0:
                zero_index = i
                break

        for i in range(zero_index, len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero_index] = nums[zero_index], nums[i]
                zero_index += 1
        print(nums)
        
        #[1, 0, 0, 3, 4]