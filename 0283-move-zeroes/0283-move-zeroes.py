class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Brute: copy all non-zeros to an array then copy back over
        # Optimal: two pointer approach where we keep a non-zero and zero pointer and when we reach a non-zero, we swap
        zero_index = 0

        # [0,0,1,0,3,12]
        # [1,1,0,0,0,3,12]
        for i in range(0, len(nums)):
            if nums[i] == 0:
                zero_index = i
                break
        
        for i in range(zero_index, len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero_index] = nums[zero_index], nums[i]
                zero_index += 1