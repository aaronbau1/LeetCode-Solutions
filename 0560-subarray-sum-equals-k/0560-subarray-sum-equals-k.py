class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        store = {0:1}
        count = 0
        psum = 0

        for i in range(len(nums)):
            psum += nums[i]
            rem = psum - k

            if rem in store:
                count += store[rem]
            
            # means a subarray summed to zero, incr count
            if psum in store:
                store[psum] += 1
            else:
                store[psum] = 1
        return count