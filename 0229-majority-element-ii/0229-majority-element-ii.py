import math

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # brute: check all numbers and frequencies O(n^3) O(n)
        # better: 
        # optimal: 
        result = []
        store = {}
        for i in range(len(nums)):
            if nums[i] in store:
                store[nums[i]] += 1
            else:
                store[nums[i]] = 1
        print(store)
        for val in store:
            if store[val] > math.floor(len(nums) // 3):
                result.append(val)
        return result