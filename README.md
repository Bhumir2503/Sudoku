#  Interactive Sudoku Generator & Solver

A fully-featured Sudoku game built with Python and Pygame, featuring an algorithmic puzzle generator, automated solver with visualization, and an intuitive user interface.

## Features

### Dynamic Puzzle Generation
- **Algorithmic board creation** using backtracking constraint satisfaction
- Generates valid 9×9 Sudoku puzzles with guaranteed unique solutions
- Randomized difficulty through selective cell removal

### Automated Solver
- Visual step-by-step solving animation
- Demonstrates the solution process in real-time with 0.1s delays
- Random cell-filling order for varied visualization

### Interactive Gameplay
- Click-to-input number entry system
- Real-time validation against the solution
- Immediate feedback on correct/incorrect answers
- Clean, intuitive grid-based UI

### Regeneration System
- One-click puzzle regeneration
- Maintains game state and UI consistency
- Fresh puzzles on demand

## Technical Implementation

### Architecture

**Generator Module** (`generator.py`)
- Object-oriented design with `Sudoku` and `Number` classes
- Constraint propagation algorithm ensuring valid board states
- Group-based validation (3×3 subgrids, rows, columns)
- Error handling for impossible board configurations

**Game Engine** (`sudoku.py`)
- Event-driven architecture using Pygame
- Separation of concerns: rendering, logic, and input handling
- State management for puzzle and solution boards

### Key Algorithms

**Board Generation**
- Uses constraint satisfaction with backtracking
- Validates against three constraints simultaneously:
- Row uniqueness
- Column uniqueness  
- 3×3 subgrid uniqueness


**Solver Visualization**
- Randomized cell revelation order
- Frame-by-frame rendering for smooth animation
- Non-blocking UI updates

## Getting Started

### Prerequisites
```bash
Python 3.x
Pygame 2.x
```

### Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/sudoku-solver.git
cd sudoku-solver
```

2. Install dependencies
```bash
pip install pygame
```

3. Run the game
```bash
python sudoku.py
```

## How to Play

1. **Start the game** - A new Sudoku puzzle generates automatically
2. **Click any empty cell** (marked with 0) to input a number
3. **Enter a number (1-9)** when prompted
4. **Receive instant feedback** - Correct numbers stay, incorrect ones are rejected
5. **Use the Regenerate button** - Get a fresh puzzle anytime
6. **Click the Solver button** - Watch the algorithm solve the puzzle step-by-step

## Code Highlights

### Smart Group Calculation
The generator uses mathematical group assignment for 3×3 subgrids:
```python
g = (int((self.col-1) / base + 1)) + ((int((self.row-1)/base)) * base)
```

### Constraint Validation
Each number placement checks three constraints in O(n) time:
- Row conflicts
- Column conflicts
- Subgrid conflicts

### Randomized Difficulty
Uses probability-based cell removal (66% chance) for varied puzzle difficulty.

##  Future Enhancements

- Multiple difficulty levels (Easy, Medium, Hard)
- Hint system
- Timer and scoring
- Save/load game state
- Undo/redo functionality
- Mobile-responsive design
- Multiplayer mode

## Testing Considerations

- Board generation validation (all puzzles must be solvable)
- Constraint satisfaction verification
- UI responsiveness testing
- Edge case handling (impossible configurations)

## Technical Skills Demonstrated

- **Algorithms**: Backtracking, constraint satisfaction, randomization
- **OOP Design**: Class hierarchies, encapsulation, separation of concerns
- **Game Development**: Event loops, rendering pipelines, state management
- **Python Libraries**: Pygame for graphics and input handling
- **Problem Solving**: Complex constraint validation, error handling

⭐ If you found this project interesting, please consider giving it a star!
