import math

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1 = 0
        count2 = 0        
        elmt1 = float("-inf")
        elmt2 = float("inf")

        for i in range(len(nums)):
            if count1 == 0 and nums[i] != elmt2:
                elmt1 = nums[i]
                count1 = 1
            elif count2 == 0 and nums[i] != elmt1:
                elmt2 = nums[i]
                count2 = 1
            elif nums[i] == elmt1:
                count1 += 1
            elif nums[i] == elmt2:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        cnt1 = 0
        cnt2 = 0
        for i in range(len(nums)):
            if nums[i] == elmt1:
                cnt1 += 1
            elif nums[i] == elmt2:
                cnt2 += 1
        print(cnt1, cnt2)
        result = []
        if cnt1 >= len(nums) // 3 + 1:
            result.append(elmt1)
        if cnt2 >= len(nums) // 3 + 1:
            result.append(elmt2)
        return result