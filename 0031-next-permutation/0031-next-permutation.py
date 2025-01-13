class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = -1
        for i in range(len(nums)-1, 0, -1):
            if nums[i-1] < nums[i]:
                pivot = i - 1
                break
        # print(pivot)
        if pivot == -1:
            nums[:] = nums[::-1]
            return

        for i in range(len(nums)-1, pivot, -1):
            if nums[i] > nums[pivot]:
                nums[i], nums[pivot] = nums[pivot], nums[i]
                break
        # print(nums)
        nums[pivot+1:] = nums[pivot+1:][::-1]



        