import random

def suggest_move_with_reason(board):
    candidates = []

    for row in range(9):
        for col in range(9):
            if board.grid[row][col] == 0:
                options = [num for num in range(1, 10) if board.is_valid(row, col, num)]
                if options:
                    candidates.append((row, col, options))

    if not candidates:
        return None

    row, col, options = min(candidates, key=lambda x: len(x[2]))
    best_num = options[0]

    # Dynamic tutor response templates
    hint_templates = [
        f"How about putting {best_num} at row {row + 1}, column {col + 1}?",
        f"A smart move could be placing {best_num} at position ({row + 1}, {col + 1}).",
        f"Try placing {best_num} at row {row + 1}, column {col + 1}.",
        f"I’d go with {best_num} at ({row + 1}, {col + 1}) — looks like a good fit.",
        f"Try entering {best_num} in cell ({row + 1}, {col + 1}) — not many options there."
    ]

    reason_templates = [
        f"Cell ({row + 1}, {col + 1}) only has {len(options)} possible value(s): {options}.",
        f"That spot has very limited options – just: {options}.",
        f"Not many numbers work in this cell. Your choices are: {options}.",
        f"The cell at ({row + 1}, {col + 1}) is nearly solved – valid numbers: {options}.",
        f"Only a few values can go here: {options} — a good place to make progress."
    ]

    hint_text = random.choice(hint_templates)
    reason_text = random.choice(reason_templates)

    return row, col, best_num, hint_text, reason_text
