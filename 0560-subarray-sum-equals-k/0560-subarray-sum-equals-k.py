class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # brute find all subarrays and sum them, O(n^3) (two loops, and one loop to sum)
        # better sum them as you move the pointer, O(n^2)
        # optimal: Use prefix sum and store values as you progress O(n) O(n)
        
        # create a store, count, psum
        # iterate with a prefix sum
        # calculate the remainder
        # if the remainder is in the store, incremenet the count
        # if the psum is in the store, increment the store[psum]
        # otherwise add the psum to the store

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

