class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_len = len(matrix)
        col_len = len(matrix[0])
        rows = [0] * row_len
        cols = [0] * col_len
        
        for i in range(row_len):
            for j in range(col_len):
                if matrix[i][j] == 0:
                    rows[i] = 1
                    cols[j] = 1
        
        for i in range(row_len):
            if rows[i] == 1:
                for j in range(col_len):
                    matrix[i][j] = 0
        
        for j in range(col_len):
            if cols[j] == 1:
                for i in range(row_len):
                    matrix[i][j] = 0
