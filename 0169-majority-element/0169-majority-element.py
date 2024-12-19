class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Brute: Check each element count in nested loop O(n^2)
        # Better: use hashmap and count freq, if greater than n/2 then return. O(n) O(n)
        # 

        count = 0
        cand_el = nums[0]
        for i in range(len(nums)):
            if cand_el != nums[i]:
                count -= 1
                if count < 0:
                    cand_el = nums[i]
                    count = 0
            else:
                count += 1
        return cand_el
            
