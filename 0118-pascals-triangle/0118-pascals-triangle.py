class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # brute: go line by line and print value based on the two previous values O(n^2)
        # optimal know that nCr is used, so create each row based on previous value
        # n! / (r)! * (n-r)! derives to previous value * (row - col) / col
        # row 5
        # [1,4,6,4,1]: 4 C 0, 4 C 1, 4 C 2, 4 C 3, 4 C 4
        result = []
        for i in range(1, numRows+1):
            val = 1
            row = [1]
            # avoid dividng by zero, start with 1
            for j in range(1, i):
                val = int(val * (i - j)/j)
                row.append(val)
            result.append(row)
        return result
