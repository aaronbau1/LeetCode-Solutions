class Solution:
    def countDigits(self, num: int) -> int:
        num_str = str(num)
        result = 0
        for i in range(len(num_str)):
            print(i, num_str[i])
            if num % int(num_str[i]) == 0:
                result += 1
        return result