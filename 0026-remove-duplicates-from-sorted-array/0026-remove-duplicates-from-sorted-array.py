class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # brute: for each element, count the number of duplicated instances and store them
            # in the front of the array O(n^2)
        # optimal: use two pointers to count the number of duplicates as you progress through the array
            # when it switches to a new element, modify the array in place for each unique element

        # [0,0,1,1,1,2,2,3,3,4]
        result = 1
        unique_num_index = 0
        current_num = nums[0]
        for i in range(0, len(nums)):
            if nums[i] != current_num:
                nums[unique_num_index] = current_num
                unique_num_index += 1
                result += 1
                current_num = nums[i]
                # Captures end number and adds to array if it is unique
                if i == len(nums) - 1:
                    nums[unique_num_index] = current_num
            if i == len(nums) - 1:
                    nums[unique_num_index] = current_num
        return result
        
            