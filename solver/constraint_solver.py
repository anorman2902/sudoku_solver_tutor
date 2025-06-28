# AI-based move suggestion logic
def suggest_move_with_reason(board):
    """
    Suggests a move using a simple AI heuristic (Minimum Remaining Value) and explains why.
    Returns: (row, col, num, reason) or None if no move found
    """
    candidates = []

    for row in range(9):
        for col in range(9):
            if board.grid[row][col] == 0:
                possible = []
                for num in range(1, 10):
                    if board.is_valid(row, col, num):
                        possible.append(num)
                if possible:
                    candidates.append((row, col, possible))

    if not candidates:
        return None

    # Pick the most constrained cell (least number of valid options)
    row, col, options = min(candidates, key=lambda x: len(x[2]))
    best_num = options[0]
    reason = (
        f"Cell ({row + 1}, {col + 1}) has only {len(options)} possible value(s): {options}. "
        f"Placing {best_num} as it's the most constrained choice."
    )

    return row, col, best_num, reason
