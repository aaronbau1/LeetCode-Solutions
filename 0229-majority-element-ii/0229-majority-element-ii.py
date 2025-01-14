import math

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # brute checking each element and counting the frequency. If they are greater than floor(n/3), put into array
            # O(n^2)
        # better using a hashmap to count the frequency, converting it to O(n) O(n) solution
        # optimal using two candidates and then manually confirming the candidates after O(2n)

        # declare two count variables
        # iterate through the loop from 0 -> n:
            # if the count is zero for first and != 2nd elmt
                # set count to 1 and change variable to current
            # elif the count is zero for the second and != 1st elmt
                # set count to 1 and change variable to current
            # elif elmt equal to 1st elemt
                # increment count 1
            # elif elmt equal to 2nd elmt
                # increment count 2
        
        # manually run through and compare values

        count1 = 0
        count2 = 0
        cand1 = float("-inf")
        cand2 = float("-inf")

        for i in range(len(nums)):
            if count1 == 0 and nums[i] != cand2:
                cand1 = nums[i]
                count1 = 1
            elif count2 == 0 and nums[i] != cand1:
                cand2 = nums[i]
                count2 = 1
            elif nums[i] == cand1:
                count1 += 1
            elif nums[i] == cand2:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        
        check = len(nums) // 3 + 1
        cnt1 = 0
        cnt2 = 0
        for i in range(len(nums)):
            if nums[i] == cand1:
                cnt1 += 1
            elif nums[i] == cand2:
                cnt2 += 1
        result = []
        if cnt1 >= check:
            result.append(cand1)
        if cnt2 >= check:
            result.append(cand2)
        return result