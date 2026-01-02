# Caesar Cipher

A Python implementation of the classic Caesar Cipher encryption and decryption algorithm. This program allows users to encode and decode messages using a shift cipher technique.

## Description

The Caesar Cipher is one of the oldest and simplest encryption techniques. It works by shifting each letter in the plaintext by a fixed number of positions down the alphabet. This implementation provides an interactive command-line interface where users can encrypt and decrypt messages using any shift value.

## Features

- **Encode Messages**: Encrypt text by shifting letters forward in the alphabet
- **Decode Messages**: Decrypt text by shifting letters backward in the alphabet
- **Custom Shift Value**: Choose any shift amount for encryption/decryption
- **Non-alphabetic Character Preservation**: Numbers, spaces, and special characters remain unchanged
- **Case Insensitive**: All text is converted to lowercase for consistency
- **Continuous Operation**: Option to encode/decode multiple messages without restarting
- **ASCII Art Logo**: Displays an attractive "caesar cipher" logo at startup

## Usage

Run the program:

```bash
python main.py
```

Follow the prompts:

1. Choose to 'encode' (encrypt) or 'decode' (decrypt)
2. Enter your message
3. Enter the shift number (how many positions to shift each letter)
4. View the result
5. Choose whether to continue with another message or exit

### Example

```
Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type you message:
hello world
Type the shift number:
5
Here is the encoded result: mjqqt btwqi

Type 'yes' if you want to go again. Otherwise, type 'no'.
yes

Type 'encode' to encrypt, type 'decode' to decrypt:
decode
Type you message:
mjqqt btwqi
Type the shift number:
5
Here is the decoded result: hello world
```

## How It Works

1. **Encoding**: Each letter is shifted forward by the specified amount
   - Example: With shift 3, 'a' becomes 'd', 'b' becomes 'e'

2. **Decoding**: Each letter is shifted backward by the specified amount
   - Example: With shift 3, 'd' becomes 'a', 'e' becomes 'b'

3. **Wrapping**: The cipher wraps around the alphabet
   - Example: With shift 3, 'z' becomes 'c'

4. **Non-alphabetic Characters**: Spaces, numbers, and punctuation are preserved as-is

## Files

- `main.py`: Main program containing the Caesar cipher logic and user interface
- `art.py`: Contains the ASCII art logo displayed at startup

## Requirements

- Python 3.x

## Educational Purpose

This project demonstrates:
- String manipulation in Python
- List operations and indexing
- Modular arithmetic for alphabet wrapping
- Function parameters and control flow
- User input validation and loops
