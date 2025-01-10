class Solution:
    def check(self, nums: List[int]) -> bool:
        # brute: have count variable and see if array goes up by one each time. Then check every element. O(n^2)
        # better: 
        # optimal: iterate through and count the drops in value, if less than or equal to 1 return true

        result = 0
        for i in range(len(nums)):
            print(i)
            if i == len(nums) - 1:
                if nums[i] > nums[0]:
                    result += 1
            elif nums[i] > nums[i+1]:
                result += 1
        return result <= 1