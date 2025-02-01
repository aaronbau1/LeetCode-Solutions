class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # optimal: create hashmap
        store = {}
        result = []
        for i in range(len(strs)):
            word = "".join(sorted(strs[i]))
            if word in store:
                result[store[word]].append(strs[i])
            else:
                result.append([strs[i]])
                store[word] = len(result) - 1
        return result