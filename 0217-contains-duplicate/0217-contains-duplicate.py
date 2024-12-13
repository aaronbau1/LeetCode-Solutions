class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Brute: iterate through nested loop and determine if each value has a duplicate O(n^2)
        # Better: sort the array and see if any value has a duplicate O(nlogn)
        # Optimal: O(n) O(n) store values in set and return true if it exists in the set
        store = set()
        for i in range(0, len(nums)):
            if nums[i] in store:
                return True
            else:
                store.add(nums[i])
        return False