class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)  # Handle cases where k > len(nums)

        # Reverse the last k elements
        nums[:len(nums) - k] = nums[:len(nums) - k][::-1]
        # print(nums)  # Debug output

        # Reverse the rest of the array
        nums[len(nums) - k:] = nums[len(nums) - k:][::-1]
        # print(nums)  # Debug output

        # Reverse the entire array
        nums[:] = nums[::-1]
        # print(nums)  # Debug output