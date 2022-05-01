class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])
        
        zero_row = [False] * m
        zero_col = [False] * n
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    zero_row[row] = True
                    zero_col[col] = True                    
        
        for row in range(m):
            for col in range(n):
                if zero_row[row] or zero_col[col]:
                    matrix[row][col] = 0