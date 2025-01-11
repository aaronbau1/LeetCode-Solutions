class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # brute: find all subarrays and sum them O(n^3)
        # better: sum subbarrays and you find them O(n^2)
        # optimal: prefix sum

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
