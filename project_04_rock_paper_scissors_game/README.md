# Project 4: Rock Paper Scissors Game

## Description

This is a classic Rock Paper Scissors game implemented in Python where the player competes against the computer. The game includes ASCII art representations of rock, paper, and scissors to make the gameplay more visually engaging.

## Features

- Interactive gameplay against computer opponent
- ASCII art representations for rock, paper, and scissors
- Random computer choice generation
- Input validation for user choices
- Clear win/lose/draw determination based on game rules

## How to Run

1. Make sure Python is installed on your computer (Python 3.x recommended)
2. Open terminal or command prompt
3. Navigate to the project directory:
   ```bash
   cd project_04_rock_paper_scissors_game
   ```
4. Run the program:
   ```bash
   python main.py
   ```

## Usage Example

```
What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors
0
User chose:
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

Computer chose:
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

You won!
```

## Game Rules

- Rock (0) beats Scissors (2)
- Paper (1) beats Rock (0)
- Scissors (2) beats Paper (1)
- Same choices result in a draw
- Invalid input (numbers less than 0 or greater than 2) results in automatic loss

## Concepts Learned

- Using `random` module to generate random choices
- List indexing and manipulation
- Conditional statements (`if`, `elif`, `else`)
- User input validation
- Multi-line strings for ASCII art
- Logical operators and comparison

## Requirements

- Python 3.x

## Notes

This project demonstrates fundamental programming concepts including random number generation, conditional logic, and input validation while creating an entertaining interactive game.
