class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(nums)
        nums.sort()
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
                        c += 1
                        d -= 1
                        while c < d and nums[c] == nums[c-1]:
                            c += 1
                        while c < d and nums[d] == nums[d+1]:
                            d -= 1
        return result