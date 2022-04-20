class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def vaild(board):
            x = [i for i in board if i != '.']
            return len(set(x)) == len(x)
        
        for row in board:
            if not vaild(row):
                return False
        for col in zip(*board):
            if not vaild(col):
                return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not vaild(square):
                    return False
        return True
        