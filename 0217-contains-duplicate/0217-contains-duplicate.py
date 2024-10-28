class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        store = set()
        for  i in range(0, len(nums)):
            if nums[i] in store:
                return True
            else:
                store.add(nums[i])
        return False
