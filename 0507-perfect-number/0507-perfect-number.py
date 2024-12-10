import math

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1: return False
        res = 1
        for i in range(2, math.ceil(num**0.5)):
            if num % i == 0:
                print(i, num // i, res)
                res += i + num // i            
        return res == num