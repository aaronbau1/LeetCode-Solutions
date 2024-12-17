class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for i in range(0, len(nums)):
            rem = target - nums[i]
            if nums[i] in store:
                return [i, store[nums[i]]]
            else:
                store[rem] = i