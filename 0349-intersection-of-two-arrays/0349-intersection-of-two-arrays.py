class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Hashset O(2n) O(n)
        store1 = set()
        store2 = set()
        result = []
        for i in range(0, len(nums1)):
            if not nums1[i] in store1:
                store1.add(nums1[i])
        for i in range(0, len(nums2)):
            if  nums2[i] in store1 and nums2[i] not in store2:
                store2.add(nums2[i])
        for val in store2:
            result.append(val)
        return result