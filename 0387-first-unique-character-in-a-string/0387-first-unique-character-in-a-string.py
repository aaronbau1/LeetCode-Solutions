class Solution:
    def firstUniqChar(self, s: str) -> int:
        # iterate through once and store, then iterate through again and find equal to 1
        # O(n), O(n)

        # 
        store = {}
        for char in s:
            if not store.get(char):
                store[char] = 1
            else:
                store[char] += 1
        for i in range(0, len(s)):
            if store[s[i]] == 1:
                return i
        return -1