class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # optimal: count local and max value of contiguous integers
        local_count = 0
        arr_max = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                arr_max = max(local_count, arr_max)
                local_count = 0
            else:
                local_count += 1
        arr_max = max(local_count, arr_max)
        return arr_max
            