class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # brute: sort and compare if they are the same O(nlogn + n)
        # optimal: hashmap of one and iterate through the second subtracting values O(2n) O(n)
        if len(s) != len(t):
            return False
        store = {}
        for char in s:
            if char in store:
                store[char] += 1
            else:
                store[char] = 1
        print(store)
        for char in t:
            if char in store:
                store[char] -= 1
            if not (char in store) or store[char] < 0:
                return False
        return True
