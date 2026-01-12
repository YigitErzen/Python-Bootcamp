# Blackjack

A Python-based Blackjack card game where you play against the computer dealer following standard Blackjack rules.

## Description

This program simulates a classic game of Blackjack (also known as 21). Players compete against the computer dealer to get as close to 21 as possible without going over. The game includes automatic Ace value adjustment, dealer AI that follows house rules, and multiple rounds of play.

## Features

- **Classic Blackjack Rules**: Standard card values and gameplay mechanics
- **Automatic Ace Handling**: Aces automatically convert from 11 to 1 when you would bust
- **Dealer AI**: Computer follows house rules (must hit on 16 or below, stands on 17+)
- **Blackjack Detection**: Instant win with a natural Blackjack (21 with two cards)
- **Multiple Rounds**: Play as many games as you want in a session
- **ASCII Art Logo**: Decorative Blackjack logo for enhanced visual appeal
- **Smart Card Dealing**: Realistic deck simulation with proper card distribution

## Usage

Run the program:

```bash
python main.py
```

Follow the prompts:
1. Type 'y' to start a new game
2. View your cards and current score
3. Decide whether to hit ('y') or stand ('n')
4. Computer dealer plays automatically
5. See the final result
6. Choose to play another round or quit

## Example

```
.-----.   _     _       _     _            _
|A .  | | |   | | __ _| |_  (_) __ _  ___| | __
|/ \  | | |_  | |/ _` | __| | |/ _` |/ __| |/ /
|\  / | |  _| | | (_| | |_ _| | (_| | (__|   <
| \|  | | |_  | |\__,_|\__(_) |\__,_|\___|_|\_\
|  .♠ | |___| |_|           |__/
`-----'

Do you want to play a game of Blackjack? Type 'y' or 'n': y

Your cards: [10, 9], current score: 19
Computer's first card: 7
Type 'y' to get another card, type 'n' to pass: n

Your final hand: [10, 9], final score: 19
Computer's final hand: [7, 10, 5], final score: 22
Opponent went over. You win 😁
```

## How It Works

1. **Card Dealing**: Each player receives 2 random cards from a standard deck
2. **Card Values**:
   - Number cards: Face value (2-10)
   - Face cards (J, Q, K): Value of 10
   - Aces: Value of 11, automatically becomes 1 if hand would bust
3. **Player Turn**: Player decides to hit (get another card) or stand
4. **Dealer Turn**: Dealer automatically hits until reaching 17 or higher
5. **Win Conditions**:
   - Natural Blackjack (21 with 2 cards) beats everything
   - Going over 21 results in automatic loss
   - Highest score under 21 wins
   - Same score results in a draw

## Files

- [main.py](main.py) - Main game logic, scoring, and game flow
- [art.py](art.py) - Contains the ASCII art Blackjack logo

## Requirements

- Python 3.x
- No external dependencies (uses built-in `random` module)

## Game Functions

- **deal_card()**: Returns a random card from the deck
- **calculate_score()**: Calculates hand value and handles Ace conversion
- **compare()**: Determines the winner by comparing scores
- **play_game()**: Main game loop handling player and dealer turns

## Game Rules

- Dealer must hit on 16 or below
- Dealer must stand on 17 or above
- Blackjack (21 with first two cards) is an instant win
- Going over 21 (bust) is an instant loss
- Higher score wins if both players are under 21
