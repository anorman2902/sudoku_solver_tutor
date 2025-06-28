from solver.board import SudokuBoard

def is_valid(board: SudokuBoard, row: int, col: int, num: int) -> bool:
    """Check if placing num at (row, col) is valid."""
    for i in range(9):
        if board.grid[row][i] == num or board.grid[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board.grid[start_row + i][start_col + j] == num:
                return False

    return True

def suggest_move(board: SudokuBoard):
    for row in range(9):
        for col in range(9):
            if board.grid[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        return row, col, num
    return None