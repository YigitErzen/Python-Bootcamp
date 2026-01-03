# Secret Auction

A Python-based blind auction program where multiple bidders can place their bids secretly without seeing others' bids.

## Description

This program simulates a secret auction where participants can place bids privately. The screen is cleared between bidders to ensure each bid remains confidential. After all bids are collected, the program determines and announces the highest bidder.

## Features

- **Secret Bidding**: Each bidder's amount is kept private from other participants
- **Multiple Bidders**: Supports unlimited number of participants
- **Screen Clearing**: Automatically clears the screen between bids to maintain secrecy
- **Winner Determination**: Automatically identifies and announces the highest bidder
- **ASCII Art Logo**: Includes decorative gavel logo for enhanced user experience

## Usage

Run the program:

```bash
python main.py
```

Follow the prompts:
1. Enter your name
2. Enter your bid amount
3. Indicate if there are more bidders (yes/no)
4. If yes, the screen clears for the next bidder
5. If no, the winner is announced

## Example

```
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                       .-------------.
                      /_______________\

What is your name?: Alice
What is your bid? $250
Are there any other bidders? Type 'yes or 'no'
yes

[Screen clears]

What is your name?: Bob
What is your bid? $300
Are there any other bidders? Type 'yes or 'no'
no

The winner is Bob with 300.0$
```

## How It Works

1. The program displays a gavel logo from the art module
2. Bidders enter their names and bid amounts one by one
3. After each bid, the user is asked if there are more bidders
4. If yes, the screen is cleared (100 newlines) to hide previous bids
5. When all bids are collected, the program iterates through all bids
6. The highest bid and bidder are determined and announced

## Files

- [main.py](main.py) - Main program logic and auction flow
- [art.py](art.py) - Contains the ASCII art gavel logo

## Requirements

- Python 3.x
- No external dependencies (uses built-in modules)

## Data Structure

The program uses a dictionary to store bids:
- **Key**: Bidder's name (string)
- **Value**: Bid amount (float)
