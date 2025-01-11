class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cand = float("-inf")
        count = 0
        for i in range(len(nums)):
            if count == 0:
                cand = nums[i]
                count = 1
            elif nums[i] == cand:
                count += 1
            else:
                count -= 1
        return cand