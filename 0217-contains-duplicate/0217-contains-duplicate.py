class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # bruter - for each value, iterate through array and see if it reappears O(n^2)
        # better - use a set and count freq - return true if element appears twice O(n) O(n)
        # optimal - 

        store = set()
        for i in range(len(nums)):
            if not (nums[i] in store):
                store.add(nums[i])
            else:
                return True
        return False