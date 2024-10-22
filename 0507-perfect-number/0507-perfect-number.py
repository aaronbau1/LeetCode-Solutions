class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num < 5:
            return False
        result = 1
        for i in range(2, int(math.sqrt(num)+1)):
            if (num % i == 0):
                result += i + num // i #get integer and its divisor
        print(result)
        return result == num