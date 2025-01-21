class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        end = len(needle)
        for i in range(len(haystack)-end + 1):
            if haystack[i:i+end] == needle:
                return i
        return -1