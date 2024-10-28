class Solution:
    def check(self, nums: List[int]) -> bool:
        switch = 0
        for i in range(0, len(nums)):
            if nums[i] < nums[i-1]:
                switch += 1
        return switch <= 1