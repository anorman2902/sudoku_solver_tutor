class SudokuBoard:
    def __init__(self, grid):
        self.grid = grid

    def is_valid(self, row, col, num):
        # Check if num is in the same row
        if any(self.grid[row][i] == num for i in range(9)):
            return False

        # Check if num is in the same column
        if any(self.grid[i][col] == num for i in range(9)):
            return False

        # Check if num is in the same 3x3 box
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.grid[start_row + i][start_col + j] == num:
                    return False

        return True

    def is_complete(self):
        return all(all(cell != 0 for cell in row) for row in self.grid)

    def print_board(self):
        for i, row in enumerate(self.grid):
            if i % 3 == 0 and i != 0:
                print("-" * 21)
            for j, cell in enumerate(row):
                if j % 3 == 0 and j != 0:
                    print("|", end=" ")
                print(cell if cell != 0 else ".", end=" ")
            print()
