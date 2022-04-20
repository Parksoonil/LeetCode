class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        assert(self.backtrack(board, 0, 0))
        return
                    
    def backtrack(self, board: List[List[str]], r: int, c: int) -> bool:
        # Go to next empty space
        while board[r][c] != '.':
            c += 1
            if c == 9: c, r = 0, r+1
            if r == 9: return True
        # Try all options, backtracking if not work
        for k in range(1, 10):
            if self.solve(board, r, c, str(k)):
                board[r][c] = str(k)
                if self.backtrack(board, r, c):
                    return True
        board[r][c] = '.'
        return False
    
    
    def solve(self, board: List[List[str]], r: int, c: int, var: str) -> bool:
        if any(board[r][j] == var for j in range(9)): return False
        if any(board[i][c] == var for i in range(9)): return False
        br, bc = 3*(r//3), 3*(c//3)
        if any(board[i][j] == var for i in range(br, br + 3) for j in range(bc, bc + 3)): return False
        return True
        