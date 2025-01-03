class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # brute - use array and fill in values based on even and odd index O(n) O(n)
        # two pointers and iterate through, then swap values if the 
        # 
        result = [0] * len(nums)
        pos = 0
        neg = 1
        for i in range(len(nums)):
            if nums[i] > 0:
                result[pos] = nums[i]
                pos += 2
            else:
                result[neg] = nums[i]
                neg += 2
        return result