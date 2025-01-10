import math

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
    # brute: check each element and see if count is greater than floor(n/3) O(n^2)
    # better: use hashmap and count freq - 
        #   if element is greater than floor(n/3) then add to array. break when two values
    # optimal: use two pointers and two frequency checks. get two candidates. Then manually check those two candidates
    # [3,2,3,0,0,3,2]
        count1 = 0
        count2 = 0
        elmt1 = 0
        elmt2 = 0

        for i in range(len(nums)):
            if count1 == 0 and elmt2 != nums[i]:
                elmt1 = nums[i]
                count1 = 1
            elif count2 == 0 and elmt1 != nums[i]:
                elmt2 = nums[i]
                count2 = 1
            elif nums[i] == elmt1:
                count1 += 1
            elif nums[i] == elmt2:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        
        # manual check
        cnt1 = 0
        cnt2 = 0
        for i in range(len(nums)):
            if nums[i] == elmt1:
                cnt1 += 1
            elif nums[i] == elmt2:
                cnt2 += 1
        result = []
        if cnt1 > math.floor(len(nums)//3):
            result.append(elmt1)
        if cnt2 > math.floor(len(nums)//3):
            result.append(elmt2)
        return result