class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # transpose the matrix and reverse each row
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                if j > i:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(n):
            matrix[i][:] = matrix[i][::-1]