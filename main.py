from solver.board import SudokuBoard
from solver.solver import solve
from solver.constraint_solver import suggest_move_with_reason

def load_board_from_file(filepath):
    grid = []
    with open(filepath, 'r') as f:
        for line in f:
            row = [int(char) for char in line.strip()]
            grid.append(row)
    return grid

if __name__ == "__main__":
    path = "puzzles/easy1.txt"
    grid = load_board_from_file(path)
    board = SudokuBoard(grid)

    print("Original Puzzle:")
    board.print_board()

    hint = suggest_move_with_reason(board)
    if hint:
        row, col, num, reason = hint
        print(f"\nTutor Hint: Try placing {num} at row {row + 1}, column {col + 1}")
        print(f"Reason: {reason}")
    else:
        print("\nNo hints available. Puzzle might be complete.")

    if solve(board):
        print("\nSolved Puzzle:")
        board.print_board()
    else:
        print("\nNo solution found.")
