class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # brute: check every subarray and sum them, see which equal k - O(n^3)
        # better: 
        # optimal: prefix sum - store sum at each point and check if the remainder
                # is within a store. If it is, increment counter

        count = 0
        psum = 0
        store = {0:1}

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