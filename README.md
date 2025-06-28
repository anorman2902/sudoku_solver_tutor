# 🧠 Sudoku Tutor Solver (CPSC 481 Project)

This is an AI-powered Sudoku tutor and solver built as a final project for CPSC 481: Artificial Intelligence.  
It helps users learn how to solve Sudoku puzzles through interactive feedback, smart hints, mistake checking, and visual polish — all in the terminal.

## 📌 Features

- ✅ Constraint-based Sudoku solver (uses backtracking + inference)
- 🧠 Smart **hints** with reasoning
- ❌ **Mistake checker** warns if a move leads to an unsolvable board
- ↩️ **Undo** support to backtrack from bad moves
- 🎨 Visual polish using:
  - Row/column labels
  - Color-coded moves (green for user input)
  - Symbols (`▢` for empty cells)
- 📁 Supports **multiple puzzles** from the `/puzzles` folder

## 🔧 Requirements

- Python 3.7 or higher  
- No external dependencies required (pure Python)

## 📂 Project Structure

```
SUDOKU_SOLVER_TUTOR/
│
├── puzzles/                   # Folder containing puzzle text files
│   ├── easy.txt               # Easy-level puzzle
│   ├── medium.txt             # Medium-level puzzle
│   └── hard.txt               # Hard-level puzzle
│
├── solver/                   # Core solver logic
│   ├── __init__.py
│   ├── board.py              # Board class (validation, display, etc.)
│   ├── constraint_solver.py  # AI tutor logic (suggests best next move)
│   ├── solver.py             # Backtracking algorithm
│   └── tutor.py              # Interface for hint generation
│
├── main.py                   # CLI entry point for the program
├── .gitignore                # Ignore Python cache and environment files
└── README.md                 # Project documentation (this file)
```

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/anorman2902/sudoku_solver_tutor.git
cd sudoku_solver_tutor
```

### 2. Run the program
```bash
python main.py
```

### 3. Follow the on-screen prompts:
- Choose a puzzle from the list.
- Enter moves in the format:  
  ```
  row col num
  ```
  (e.g., `3 4 7` places number 7 at row 3, column 4)
- Use these commands:
  - `hint` — get a tutor suggestion with explanation
  - `solve` — auto-solve the puzzle
  - `undo` — undo the last move
  - `quit` — exit the program

## 🧠 AI Logic Explained

- **Constraint Solver**: Uses naked singles (cells with only 1 possible value) and forward checking to suggest logical moves.
- **Backtracking Solver**: Recursive Sudoku solver used to check if a board is solvable after user input.
- **Mistake Checker**: After every valid user move, a clone of the board is solved silently. If unsolvable, the user is warned.
- **Undo Stack**: Stores board states for safe rollback.

## 📌 Example Puzzle File Format

Each puzzle is stored as a `.txt` file with 9 lines of 9 digits (0 = empty cell):

```
530070000
600195000
098000060
800060003
400803001
700020006
060000280
000419005
000080079
```

Custom puzzle files may be added to the `/puzzles` folder

## 📈 Potential Enhancements (Future Goals)

- GUI using Tkinter or PyQt
- Puzzle difficulty classifier
- AI explanation generator (natural language)
- ML-trained Sudoku strategy engine

## 👨‍🏫 Developed For

**CPSC 481 - Artificial Intelligence**  
California State University, Fullerton  
Instructor: Prof. Anand Panangadan
