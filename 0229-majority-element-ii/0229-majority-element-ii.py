class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1 = 0
        cand2 = 0
        count1 = 0
        count2 = 0

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
        
        # manually check cand1 and cand2
        cnt1 = 0
        cnt2 = 0
        for i in range(len(nums)):
            if nums[i] == cand1:
                cnt1 += 1
            elif nums[i] == cand2:
                cnt2 += 1
        result = []
        if cnt1 >= (len(nums) // 3 + 1):
            result.append(cand1)
        if cnt2 >= (len(nums) // 3 + 1):
            result.append(cand2)
        return result