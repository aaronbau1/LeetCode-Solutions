class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 10 and x >= 0:
            return True
        reversed = ""
        num = x
        while (num > 0):
            reversed += str(num % 10)
            num = num // 10
        return reversed == str(x)
