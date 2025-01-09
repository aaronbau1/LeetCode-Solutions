import math

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # brute: check all numbers and frequencies O(n^3) O(n)
        # better: 
        # optimal: 
        target_count = (len(nums) // 3) + 1
        result = []
        store = {}
        for i in range(len(nums)):
            if nums[i] in store:
                store[nums[i]] += 1
            else:
                store[nums[i]] = 1
            
            if store[nums[i]] == target_count:
                result.append(nums[i])
            if len(result) == 2:
                break
        return result