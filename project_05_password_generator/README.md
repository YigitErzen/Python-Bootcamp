# Password Generator

A Python-based password generator that creates secure, randomized passwords based on user preferences.

## Description

This program generates strong, random passwords by combining letters (both uppercase and lowercase), numbers, and symbols. Users can specify how many of each character type they want in their password, and the program will create a randomized password that meets those specifications.

## Features

- **Customizable Length**: Choose exactly how many letters, symbols, and numbers you want
- **Character Variety**: Includes lowercase letters, uppercase letters, numbers, and special symbols
- **Random Generation**: Uses Python's random module for unpredictable character selection
- **Shuffled Output**: Characters are randomly shuffled to ensure passwords are not predictable

## Usage

Run the program:

```bash
python main.py
```

Follow the prompts to specify your password requirements:
1. Enter the number of letters you want
2. Enter the number of symbols you want
3. Enter the number of numbers you want

The program will generate and display a secure password based on your specifications.

## Example

```
Welcome to the PyPassword Generator!
How many letters would you like in your password?
8
How many symbols would you like?
2
How many numbers would you like?
3
Your password is: kT3n#m9L$aR2p
```

## Character Sets

- **Letters**: All lowercase (a-z) and uppercase (A-Z) letters
- **Numbers**: Digits 0-9
- **Symbols**: ! # $ % & ( ) * +

## Requirements

- Python 3.x
- No external dependencies (uses built-in `random` module)
