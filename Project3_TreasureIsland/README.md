# Treasure Island

A text-based adventure game where you navigate through different choices to find the hidden treasure.

## Description

This Python application is an interactive story game where players make decisions at key moments to determine their fate. The goal is to find the treasure by making the right choices. One wrong move and it's game over!

## Features

- ASCII art welcome banner featuring a treasure island scene
- Interactive story with multiple decision points
- Different endings based on player choices
- Input validation and case-insensitive responses
- Immediate feedback on choices

## How to Use

1. Run the program:
   ```bash
   python main.py
   ```

2. Follow the story prompts and make your choices:
   - At the crossroad: Choose "left" or "right"
   - At the lake: Choose to "swim" or "wait"
   - At the doors: Choose "red", "blue", or "yellow"

3. Try to find the treasure by making the right decisions!

## Game Flow

```
Start at crossroad → Choose left
                  ↓
         Encounter lake → Wait for boat
                       ↓
              Three doors → Choose yellow door
                         ↓
                    WIN! (Find the treasure)
```

Any deviation from this path leads to Game Over.

## Example Gameplay

```
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
...
*******************************************************************************
Welcome to Treasure Island.
Your mission is to find the treasure.
You're at a crossroad, where do you want to go? Type "left" or "right".
left
There's a lake blocking your path.There is an island in the middle of the lake. You can see something shiny on the other side. Do you "swim" or "wait" ?
wait
You waited. Smart move. A boat showed up and got you across.Now there are three doors: "red", "blue", and "yellow" .Which colour do you choose?
yellow
You found the treasure. You Win!
```

## Requirements

- Python 3.x

## Learning Objectives

This project demonstrates:
- Conditional statements (`if`, `elif`, `else`)
- Nested conditional logic
- User input handling with `input()`
- String methods (`.lower()`)
- Multi-line strings and ASCII art with raw strings (`r'''`)
- Game logic and flow control

## Notes

This is a beginner-friendly project that introduces control flow and decision trees in Python programming. The game has multiple endings, encouraging players to explore different paths.
