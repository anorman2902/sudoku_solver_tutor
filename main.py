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

    while True:
        hint = suggest_move_with_reason(board)
        if hint:
            row, col, num, reason = hint
            print(f"\nTutor Hint: Try placing {num} at row {row + 1}, column {col + 1}")
            print(f"Reason: {reason}")
        else:
            print("\nNo hints available. Puzzle might be complete.")

        print("\nEnter your move as 'row col num' (1-based indexing)")
        print("Or type 'hint' to repeat hint, 'solve' to auto-solve, or 'quit' to exit.")

        user_input = input("> ").strip().lower()

        if user_input == "quit":
            print("Exiting the program.")
            break
        elif user_input == "solve":
            if solve(board):
                print("\nSolved Puzzle:")
                board.print_board()
            else:
                print("\nNo solution found.")
            break
        elif user_input == "hint":
            continue

        try:
            parts = user_input.strip().split()

            if len(parts) == 3 and all(part.isdigit() for part in parts):
                r, c, n = map(int, parts)
                if not (1 <= r <= 9 and 1 <= c <= 9 and 1 <= n <= 9):
                    print("❌ Numbers must be between 1 and 9.")
                    continue

                r -= 1
                c -= 1

                if board.grid[r][c] != 0:
                    print("❌ That cell is already filled. Try a different one.")
                elif not board.is_valid(r, c, n):
                    print("❌ Invalid move. That number breaks Sudoku rules.")
                else:
                    board.grid[r][c] = n
                    board.print_board()
            else:
                print("Invalid input. Please enter as: row col num (e.g., 3 4 7)")
        except Exception as e:
            print(f"Unexpected error: {e}")
