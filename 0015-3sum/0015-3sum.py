class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # brute find all combinations of 3 numbers and sum them and sort them. O(n^3)
        # better use a storage set to store combinations, know that k = -i + -j so we can reduce to two loops
        # optimal use a fixed pointer that we loop through with a two pointer approach 
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                threeSum = nums[i] + nums[j] + nums[k]
                if threeSum > 0:
                    k -= 1
                elif threeSum < 0:
                    j += 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
        return result