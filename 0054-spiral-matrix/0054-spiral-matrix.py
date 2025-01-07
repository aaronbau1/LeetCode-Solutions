class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        left = 0
        top = 0
        right = len(matrix[0]) - 1
        bot = len(matrix) - 1

        while left <= right and top <= bot:
            # top
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

            # right
            for i in range(top, bot + 1):
                result.append(matrix[i][right])
            right -= 1
            
            # bottom
            if top <= bot:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bot][i])
                bot -= 1

            # left
            if left <= right:
                for i in range(bot, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
        return result

