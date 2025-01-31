class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # brute create a hashmap and iterate through twice O(2n) O(n)
        # optimal use a set and add to it, return value if it's in the set O(n) O(n)
        store = set()
        for i in range(len(nums)):
            if nums[i] in store:
                return True
            else:
                store.add(nums[i])
        return False