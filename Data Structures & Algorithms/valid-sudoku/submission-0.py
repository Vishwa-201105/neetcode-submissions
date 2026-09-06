class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # column-wise check
        for r in range(9):
            seen = set()
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in seen:
                    return False
                seen.add(board[r][c])
        
        # row-wise check
        for c in range(9):
            seen = set()
            for r in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in seen:
                    return False
                seen.add(board[r][c])
        
        # box-wise check
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    r = (square // 3) * 3 + i
                    c = (square % 3) * 3 + j
                    if board[r][c] == ".":
                        continue
                    if board[r][c] in seen:
                        return False
                    seen.add(board[r][c])
        return True
