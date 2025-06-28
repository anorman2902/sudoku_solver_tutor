class SudokuBoard:
    def __init__(self, grid):
        self.grid = grid
        self.history = []  # Track history for undo
        self.original_cells = {
            (r, c)
            for r in range(9)
            for c in range(9)
            if grid[r][c] != 0
        }

    def is_valid(self, row, col, num):
        if any(self.grid[row][i] == num for i in range(9)):
            return False
        if any(self.grid[i][col] == num for i in range(9)):
            return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.grid[start_row + i][start_col + j] == num:
                    return False
        return True

    def is_complete(self):
        return all(all(cell != 0 for cell in row) for row in self.grid)

    def make_move(self, row, col, num):
        # Save current value before making the move
        self.history.append((row, col, self.grid[row][col]))
        self.grid[row][col] = num

    def undo_move(self):
        if not self.history:
            return False
        row, col, prev_val = self.history.pop()
        self.grid[row][col] = prev_val
        return True

    def print_board(self):
        print("\n    1 2 3   4 5 6   7 8 9")
        print("  +-------+-------+-------+")

        for i, row in enumerate(self.grid):
            row_str = f"{i + 1} |"
            for j, cell in enumerate(row):
                if j % 3 == 0 and j != 0:
                    row_str += " |"

                if cell == 0:
                    row_str += " ▢"
                else:
                    if (i, j) in self.original_cells:
                        row_str += f" {cell}"
                    else:
                        row_str += f" \033[92m{cell}\033[0m"  # Green for user-added
            row_str += " |"
            print(row_str)

            if (i + 1) % 3 == 0:
                print("  +-------+-------+-------+")
