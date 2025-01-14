class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # brute calculate values 1 by 1 based on previous, have to do a summation for all elements O(n^3)
        # better: calculate rows based on nCr, reducing to O(n^2)
        # optimal nCr becomes row-1 C col - 1, simplified to row-col/col * prev value

        result = []
        for i in range(1, numRows+1):
            row = []
            val = 1
            for j in range(i): # 0,1,2, 3
                if j == 0:
                    val = 1
                else:
                    val = int(val * (i - j)/j)
                row.append(val)
            result.append(row)
        return result