class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # brute - iterate through and select each index, then sum on left and right side O(n^2)
        # better - use a hashmap and record sum for right iteration, then iterate left and see where it matches O(n) O(n)
        # optimal - sum all values, and then iterate once through and compare right and left
        total = 0
        for i in range(len(nums)):
            total += nums[i]

        left = 0
        right = total
        for i in range(len(nums)):
            right -= nums[i]
            if left == right:
                return i
            left += nums[i]
        return -1
