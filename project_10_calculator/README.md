# Calculator

A command-line calculator application built with Python that supports basic arithmetic operations with continuous calculation capability.

## Description

This interactive calculator allows users to perform basic mathematical operations (addition, subtraction, multiplication, and division) with the ability to chain calculations. Users can continue calculating with the previous result or start a fresh calculation at any time.

## Features

- **Four Basic Operations**: Addition (+), Subtraction (-), Multiplication (*), and Division (/)
- **Continuous Calculation**: Continue calculating with the previous result
- **ASCII Art Logo**: Displays a decorative calculator logo at startup
- **User-Friendly Interface**: Clear prompts and formatted output
- **Recursive Design**: Ability to start new calculations without restarting the program

## How to Run

1. Make sure you have Python installed on your system
2. Navigate to the project directory:
   ```bash
   cd project_10_calculator
   ```
3. Run the program:
   ```bash
   python main.py
   ```

## Usage

1. When the program starts, you'll see the calculator logo
2. Enter the first number when prompted
3. Choose an operation from the available symbols (+, -, *, /)
4. Enter the next number
5. View the result of your calculation
6. Choose whether to:
   - Type 'y' to continue calculating with the current result
   - Type 'n' to start a new calculation

## Example

```
What is the first number?: 10
+
-
*
/
Pick an operation: +
What is the next number?: 5
10.0 + 5.0 = 15.0
Type 'y' to continue calculating with 15.0, or type 'n' to start a new calculation y
+
-
*
/
Pick an operation: *
What is the next number?: 2
15.0 * 2.0 = 30.0
```

## Files

- [main.py](main.py) - Main calculator logic and program flow
- [art.py](art.py) - ASCII art logo for the calculator

## Project Structure

The calculator uses a dictionary to map operation symbols to their corresponding functions, making it easy to extend with additional operations if needed.
