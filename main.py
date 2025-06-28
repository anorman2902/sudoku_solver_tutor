from solver.board import SudokuBoard
from solver.solver import solve
from solver.constraint_solver import suggest_move_with_reason

import os
from copy import deepcopy

def load_board_from_file(filepath):
    grid = []
    with open(filepath, 'r') as f:
        for line in f:
            row = [int(char) for char in line.strip()]
            grid.append(row)
    return grid

def choose_puzzle():
    puzzle_dir = "puzzles"
    files = [f for f in os.listdir(puzzle_dir) if f.endswith(".txt")]

    print("Available puzzles:")
    for i, filename in enumerate(files, 1):
        print(f"{i}. {filename}")

    while True:
        try:
            choice = int(input("\nSelect a puzzle number: "))
            if 1 <= choice <= len(files):
                return os.path.join(puzzle_dir, files[choice - 1])
            else:
                print("❌ Invalid choice.")
        except ValueError:
            print("Please enter a number.")

if __name__ == "__main__":
    path = choose_puzzle()
    grid = load_board_from_file(path)
    board = SudokuBoard(grid)

    print("\nOriginal Puzzle:")
    board.print_board()

    while True:
        print("\nEnter your move as 'row col num' (e.g., 3 4 7)")
        print("Commands: 'hint' for a suggestion, 'undo' to undo last move, 'solve' to auto-solve, 'quit' to exit.")
        command = input("> ").strip().lower()

        if command == "quit":
            print("Exiting the program.")
            break

        elif command == "solve":
            if solve(board):
                print("\nSolved Puzzle:")
                board.print_board()
            else:
                print("\n❌ No solution found.")
            break

        elif command == "hint":
            result = suggest_move_with_reason(board)
            if result:
                row, col, num, hint_text, reason_text = result
                print(f"\nTutor Hint: {hint_text}")
                print(f"Reason: {reason_text}")
            else:
                print("\n✅ No hints available. Puzzle might be complete.")
            continue

        elif command == "undo":
            if board.undo_move():
                print("\nLast move undone.")
            else:
                print("\n❌ No moves to undo.")
            board.print_board()
            continue

        else:
            try:
                row, col, num = map(int, command.split())
                row -= 1
                col -= 1
                if not (0 <= row < 9 and 0 <= col < 9 and 1 <= num <= 9):
                    raise ValueError

                if board.grid[row][col] != 0:
                    print("\n❌ Cell already filled. Try another.")
                elif board.is_valid(row, col, num):
                    board.make_move(row, col, num)
                    print()
                    board.print_board()

                    # Mistake checker
                    temp_board = SudokuBoard(deepcopy(board.grid))
                    if not solve(temp_board):
                        print(f"\n⚠️ Warning: This move makes the puzzle unsolvable.")
                else:
                    print(f"\n❌ Invalid move: {num} conflicts with Sudoku rules at ({row + 1}, {col + 1})")

            except ValueError:
                print("\n❌ Invalid input. Please enter in format: row col num (e.g., 3 4 7)")
