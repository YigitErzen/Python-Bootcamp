# Tip Calculator

A simple command-line tip calculator that helps you split bills among multiple people, including tip calculations.

## Description

This Python application calculates the total bill including tip and divides it equally among a specified number of people. It's a practical tool for restaurant outings and group dining experiences.

## Features

- Calculate tip based on custom percentage (10%, 12%, 15%, or any other percentage)
- Split the total bill (including tip) among multiple people
- Displays the amount each person should pay, rounded to 2 decimal places

## How to Use

1. Run the program:
   ```bash
   python main.py
   ```

2. Follow the prompts:
   - Enter the total bill amount
   - Enter the tip percentage you'd like to give
   - Enter the number of people to split the bill

3. The program will calculate and display how much each person should pay.

## Example

```
Welcome to the tip calculator!
What was the total bill? $150.00
What percentage tip would you like to give? 10, 12, 15 15
How many people to split the bill? 5
Each person should pay: $34.50
```

## Requirements

- Python 3.x

## Learning Objectives

This project demonstrates:
- User input handling with `input()`
- Type conversion (`float()`, `int()`)
- Basic arithmetic operations
- String formatting with f-strings
- Rounding numbers to specific decimal places
