class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # brute - use a 2nd array and make change in there based on zeros
        # better - use a result array that signals the zeros, then update the given array based on that
        # optimal - use the 1st row / col of the matrix as the signal array + one variable
        first_col = 1
        rows = len(matrix)
        cols = len(matrix[0])

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0

                    if col != 0:
                        matrix[0][col] = 0
                    else:
                        first_col = 0

        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][col] != 0:
                    if matrix[row][0] == 0 or matrix[0][col] == 0:
                        matrix[row][col] = 0
        
        if matrix[0][0] == 0:
            for col in range(cols):
                matrix[0][col] = 0

        if first_col == 0:
            for row in range(rows):
                matrix[row][0] = 0