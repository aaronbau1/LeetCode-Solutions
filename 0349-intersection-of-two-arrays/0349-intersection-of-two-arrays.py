class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Brute: For each value, check if it exists in second array - if unique add to result array O(n^2)
        # Optimal: Create a set of the first array, then iterate through next array 
            # and add unique elements, then convert from set to result array O(3n) O(n)
        
        store1 = set()
        store2 = set()
        result = []

        for val in nums1:
            store1.add(val)
        
        for val in nums2:
            if (val in store1) and (val not in store2):
                store2.add(val)

        for val in store2:
            result.append(val)
        return result