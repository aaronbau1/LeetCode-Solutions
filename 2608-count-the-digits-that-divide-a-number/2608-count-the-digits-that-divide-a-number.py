class Solution:
    def countDigits(self, num: int) -> int:
        res = 0
        strnum = str(num)
        newnum = num
        for j in range(0,len(strnum)):
            digit = newnum % 10
            rem = newnum // 10
            if num % digit == 0:
                res += 1
            newnum = rem
        return res