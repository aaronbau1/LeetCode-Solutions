class Solution:
    def check(self, nums: List[int]) -> bool:
        # O(n^2) check each index and see if it is constantly incr from there
        # O(nlogn) sort array and then see if it is const increasing
        # see if there is one or 0 decrement - if so return true, otherwise return false

        result = 0
        if nums[0] < nums[-1]:
            result += 1
        for i in range(0, len(nums) - 1):
            if nums[i + 1] < nums[i]:
                result += 1
        return True if result < 2 else False
