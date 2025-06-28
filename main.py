from solver.board import SudokuBoard
from solver.solver import solve

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

    if solve(board):
        print("\nSolved Puzzle:")
        board.print_board()
    else:
        print("\nNo solution found.")
