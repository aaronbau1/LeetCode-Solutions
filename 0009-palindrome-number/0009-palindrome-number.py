class Solution:
    def isPalindrome(self, x: int) -> bool:
        # return str(x) == str(x)[::-1]
        strx = str(x)
        for i in range(0, len(strx)):
            if i > len(strx) // 2 - 1:
                break
            if strx[i] != strx[len(strx) - i - 1]:
                return False
        return True