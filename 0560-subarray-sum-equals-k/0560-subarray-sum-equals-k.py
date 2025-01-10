class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # brute: sum all possible array O(n^3)
        # better: calculate sum while creating all possible arrays O(n^2)
        # optimal: prefix sum, but integrate a count variable to account for 
        # multiple prefix sums with same value
        # note, must start at 0 to account for subarrays including first value
        count = 0
        psum = 0
        store = {0:1}
        # [1,2,3]
        for i in range(len(nums)):
            psum += nums[i]
            rem = psum - k

            if rem in store:
                count += store[rem]
            
            if psum in store:
                store[psum] += 1
            else:
                store[psum] = 1
        return count
            