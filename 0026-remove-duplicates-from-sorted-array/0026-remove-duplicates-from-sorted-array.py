class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uniq_index = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            else:
                nums[uniq_index] = nums[i]
                uniq_index += 1
        return uniq_index