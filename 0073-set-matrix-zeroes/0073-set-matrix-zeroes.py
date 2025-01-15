class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # brute: make a copy of the array - when an element is zero, mark the rows int he copy O(n^2) O(n)
        # better: use an external row and column array and mark when an element is zero. Then iterate through and mark the array
        # optimal: Use the first row and columns + one variable to mark array

        rows = len(matrix)
        cols = len(matrix[0])
        first_col = False

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0

                    if col != 0:
                        matrix[0][col] = 0
                    else:
                        first_col = True
        
        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0
        
        if matrix[0][0] == 0:
            for col in range(cols):
                matrix[0][col] = 0
        if first_col:
            for row in range(rows):
                matrix[row][0] = 0
        