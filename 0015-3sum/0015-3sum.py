class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # bruter: find all triplets in three loops, sum them, sort them and see if they already exist in the array O(n^3 + nlogn)
        # better: use a hashmap and store results in them, then loop through and find all triplets. Before storing, we sort and check O(n^2)
        # optimal: two pointer with initial sort
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