class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = 0
        local_sum = 0
        for i in range(len(nums)):
            local_sum += nums[i]
            max_sum = max(local_sum, max_sum)

            if i == len(nums)-1:
                break
            elif nums[i] >= nums[i+1]:
                local_sum = 0
        return max_sum