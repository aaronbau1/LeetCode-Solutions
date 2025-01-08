class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []

        for row_index in range(1, numRows + 1):
            row = [1]
            val = 1
            for col_index in range(1, row_index):
                val = val * (row_index - col_index) // col_index
                row.append(val)
            result.append(row)
        return result