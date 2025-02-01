class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = {}
        for s in strs:
            count = [0] * 26
            for char in s:
                i = ord(char) - ord('a')
                count[i] += 1
            if tuple(count) in store:
                store[tuple(count)].append(s)
            else:
                store[tuple(count)] = [s]
        return list(store.values())
