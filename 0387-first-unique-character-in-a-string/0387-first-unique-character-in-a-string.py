class Solution:
    def firstUniqChar(self, s: str) -> int:
        store = {}
        for i in range(0, len(s)):
            if s[i] in store:
                store[s[i]] += 1
            else:
                store[s[i]] = 1
        for i in range(0, len(s)):
            if store[s[i]] == 1:
                return i
        return -1