class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # bruter: remove zeros from list and keep count, then add them all in at the end
        # optimal: two pointer, if there is a zero then swap with non-zero element
        #  [0,0,1,0,1,3,12]
        
        # find first non-zero index and first zero index (0,2)
        # swap [1,0,0,0,1,3,12], increment zero index
        # 
        # iterate from the first non-zero index
        # go until you find a non-zero
        # swap
        # increment zero index by one
        # go until end of array
        zero_index = 0
        while zero_index < len(nums) and nums[zero_index] != 0:
            zero_index += 1
        i = zero_index
        while i < len(nums):
            if nums[i] != 0:
                nums[i], nums[zero_index] = nums[zero_index], nums[i]
                zero_index += 1
            i += 1
        
