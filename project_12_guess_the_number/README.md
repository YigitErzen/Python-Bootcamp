# Guess the Number

A Python-based number guessing game where you try to guess a randomly generated number between 1 and 100 within a limited number of attempts.

## Description

This program is an interactive guessing game where the computer thinks of a random number between 1 and 100, and you have to guess it. You can choose between two difficulty levels that determine how many attempts you get. The game provides feedback after each guess to help you narrow down the correct answer.

## Features

- **Two Difficulty Levels**: Choose between Easy (10 attempts) or Hard (5 attempts) mode
- **Interactive Feedback**: Get hints whether your guess is too high or too low
- **Attempt Tracking**: See how many guesses you have remaining
- **ASCII Art Logo**: Decorative game logo for enhanced visual appeal
- **Input Validation**: Clean number input handling
- **Real-time Hints**: Immediate feedback after each guess

## Usage

Run the program:

```bash
python main.py
```

Follow the prompts:
1. View the welcome message and game logo
2. Choose your difficulty level ('easy' or 'hard')
3. Make your guess by entering a number between 1 and 100
4. Receive feedback (too high, too low, or correct)
5. Continue guessing until you win or run out of attempts

## Example

```
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Choose a difficulty. Type 'easy' or 'hard': easy
You have 10 attempts remaining to guess the number.
Make a guess: 50
Too low.
Guess again.
You have 9 attempts remaining to guess the number.
Make a guess: 75
Too high.
Guess again.
You have 8 attempts remaining to guess the number.
Make a guess: 62
You got it! The answer was 62
```

## How It Works

1. **Number Generation**: Computer randomly selects a number between 1 and 100
2. **Difficulty Selection**: Player chooses Easy (10 turns) or Hard (5 turns) mode
3. **Guessing Loop**:
   - Player enters their guess
   - Program compares guess with the answer
   - Provides "Too high" or "Too low" feedback
   - Decrements remaining attempts
4. **Win/Lose Conditions**:
   - Win: Guess the correct number before running out of attempts
   - Lose: Use all attempts without guessing correctly

## Files

- [main.py](main.py) - Main game logic, difficulty settings, and game loop
- [art.py](art.py) - Contains the ASCII art logo

## Requirements

- Python 3.x
- No external dependencies (uses built-in `random` module)

## Game Functions

- **check_answer()**: Compares user's guess with the actual answer and returns remaining turns
- **set_difficulty()**: Sets the number of attempts based on chosen difficulty level
- **game()**: Main game loop that controls the entire game flow

## Difficulty Levels

- **Easy Mode**: 10 attempts to guess the number
- **Hard Mode**: 5 attempts to guess the number

## Tips for Playing

- Start with 50 (the middle value) to maximize information from your first guess
- Use binary search strategy: after each hint, guess the middle of the remaining range
- In Easy mode, you have more room for random guesses
- In Hard mode, strategic guessing is essential to win
