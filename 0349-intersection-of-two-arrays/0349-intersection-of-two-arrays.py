class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # brute: check all values of first array, and compare to 2nd array O(n^2)
        # better:
        # optimal: use a set for first, then compare 2nd list to the set in another set. thne convert to list
        store1 = set()
        store2 = set()

        for i in range(len(nums1)):
            if nums1[i] not in store1:
                store1.add(nums1[i])
        
        for i in range(len(nums2)):
            if (nums2[i] in store1) and (nums2[i] not in store2):
                store2.add(nums2[i])
        
        result = []
        for val in store2:
            result.append(val)
        return result