# Hangman Game

A classic word-guessing game implemented in Python where players try to guess a hidden word letter by letter before running out of lives.

## Description

This program is a command-line implementation of the popular Hangman game. The computer randomly selects a word from a predefined word list, and the player must guess the word one letter at a time. With each incorrect guess, the player loses a life, and a hangman figure is progressively drawn. The game ends when the player either guesses the word correctly or runs out of lives.

## Features

- **Random Word Selection**: Words are randomly chosen from a comprehensive word list
- **Visual Feedback**: ASCII art displays the hangman's progression with each wrong guess
- **Lives System**: Players start with 6 lives
- **Input Validation**: Prevents re-guessing already guessed letters
- **Interactive Display**: Shows current game state with underscores for unguessed letters
- **ASCII Art Logo**: Displays a welcome logo at game start

## Usage

Run the program:

```bash
python main.py
```

Follow the gameplay:
1. The game displays the logo and shows underscores representing the hidden word
2. Enter a letter guess when prompted
3. The game reveals if your guess is correct and updates the word display
4. Continue guessing until you either win or lose all 6 lives

## Example Gameplay

```
 _
| |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |
                   |___/

Word to guess: _______
****************************6/6 LIVES LEFT****************************
Guess a letter: a
Word to guess: _a___a_
****************************6/6 LIVES LEFT****************************
Guess a letter: e
You guessed e, that's not in the word. You lose a life.
****************************5/6 LIVES LEFT****************************
```

## Game Rules

- Players have **6 lives** to guess the word
- Each incorrect letter guess costs one life
- Guessing the same letter twice is allowed but doesn't cost a life
- Win by revealing all letters before running out of lives
- Lose when all 6 lives are depleted

## Project Structure

- `main.py`: Main game logic and loop
- `hangman_words.py`: Contains the word list for random selection
- `hangman_art.py`: ASCII art for the hangman stages and game logo

## Requirements

- Python 3.x
- No external dependencies (uses built-in `random` module)
