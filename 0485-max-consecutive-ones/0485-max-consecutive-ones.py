class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Brute: 
        # Optimal: iterate through and keep track of local max / global max O(n)
        local_count = 0
        max_count = 0

        for i in range(0, len(nums)):
            if nums[i] == 0:
                if local_count > max_count:
                    max_count = local_count
                local_count = 0
            else:
                local_count += 1
                if i == len(nums) - 1 and local_count > max_count:
                    max_count = local_count
        return max_count
