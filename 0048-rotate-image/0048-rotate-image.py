class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 0,1 1,0 02, 2,0
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                if i != j and j > i:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i][:] = matrix[i][::-1]

        