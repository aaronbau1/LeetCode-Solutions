class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # brute: four loops, calculate all subarrays, sort them and add to a set to check if they exist
        # better: elimite fourth loop by using target - i - j - k and using hashset for last value - then record all values as you iterate and if you find
        # a result, then you can add it to the hashset for quad sets. O(n^3) O(2n)
        # optimal 2 static, 2 pointers

        result = []
        nums.sort()
        n = len(nums)
        for a in range(n):
            if a > 0 and nums[a] == nums[a-1]:
                continue
            for b in range(a + 1, n):
                if b > a + 1 and nums[b] == nums[b-1]:
                    continue
                c = b + 1
                d = n - 1
                while c < d:
                    fourSum = nums[a] + nums[b] + nums[c] + nums[d]
                    if fourSum > target:
                        d -= 1
                    elif fourSum < target:
                        c += 1
                    else:
                        result.append([nums[a], nums[b], nums[c], nums[d]])
                        d -= 1
                        c += 1
                        while c < d and nums[c] == nums[c-1]:
                            c += 1
                        while c < d and nums[d] == nums[d+1]:
                            d -= 1
        return result
            