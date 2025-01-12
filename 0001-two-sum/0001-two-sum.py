class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        store = {}
        for i in range(len(nums)):
            rem = target - nums[i]

            if rem in store:
                return [store[rem], i]
            else:
                store[nums[i]] = i