def find_empty(board):
    """Find the next empty cell (represented by 0)."""
    for i in range(9):
        for j in range(9):
            if board.grid[i][j] == 0:
                return i, j
    return None

def solve(board):
    """Recursive backtracking Sudoku solver."""
    empty = find_empty(board)
    if not empty:
        return True  # Puzzle solved

    row, col = empty
    for num in range(1, 10):
        if board.is_valid_move(row, col, num):
            board.grid[row][col] = num

            if solve(board):
                return True

            board.grid[row][col] = 0  # Backtrack

    return False
