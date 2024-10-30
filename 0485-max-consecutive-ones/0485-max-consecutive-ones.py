class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        local_max = 0
        max = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                local_max = 0
            else:
                local_max += 1
                if local_max > max:
                    max = local_max
        return max