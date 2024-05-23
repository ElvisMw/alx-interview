# 0x04. UTF-8 Validation

## Description

This project involves validating a given dataset to determine if it represents a valid UTF-8 encoding. UTF-8 is a variable-width character encoding used for electronic communication. The objective is to create a Python method that checks whether a list of integers corresponds to a valid UTF-8 encoding.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3)
- All files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the project folder is mandatory
- Your code should use the `PEP 8` style (version 1.7.x)
- All files must be executable

## Concepts

To complete this project, you should be familiar with the following concepts:

- **Bitwise Operations in Python:**
  - AND (`&`), OR (`|`), XOR (`^`), NOT (`~`), shifts (`<<`, `>>`)
- **UTF-8 Encoding Scheme:**
  - Encoding rules and patterns for 1 to 4 byte characters
- **Data Representation:**
  - Handling byte-level data and least significant bits (LSB)
- **List Manipulation in Python:**
  - Iterating, accessing elements, and list comprehensions
- **Boolean Logic:**
  - Logical operations for decision making

## Resources

- [Python Bitwise Operators](https://wiki.python.org/moin/BitwiseOperators)
- [UTF-8 Wikipedia](https://en.wikipedia.org/wiki/UTF-8)
- [Characters, Symbols, and the Unicode Miracle](https://www.joelonsoftware.com/2003/10/08/characters-vs-bytes/)
- [The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/)

## Tasks

### 0. UTF-8 Validation

#### Mandatory

Write a method that determines if a given dataset represents a valid UTF-8 encoding.

- **Prototype:** `def validUTF8(data):`
- **Return:** `True` if data is a valid UTF-8 encoding, else `False`
- A character in UTF-8 can be 1 to 4 bytes long
- The dataset can contain multiple characters
- The data will be represented by a list of integers
- Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer

#### Example Usage

```python
#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))  # True

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))  # True

data = [229, 65, 127, 256]
print(validUTF8(data))  # False
