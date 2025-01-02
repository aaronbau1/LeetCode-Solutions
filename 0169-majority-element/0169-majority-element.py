class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # brute - iterate for each value and count number of times it appears in array O(n^2)
        # better - use hashmap and store frequencies, then iterate through and return the greatest O(n) O(n)
        # optimal - polling algorithm, iterate through and choose candidate and track local count

        count = 1
        cand = nums[0]
        for i in range(1, len(nums)):
            if count == 0:
                cand = nums[i]
                count = 1
            elif nums[i] == cand:
                count += 1
            else:
                count -= 1
        return cand
