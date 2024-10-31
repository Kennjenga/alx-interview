# 0x04. UTF-8 Validation

For the “0x04. UTF-8 Validation” project, you will need to apply your knowledge in bitwise operations, understanding of the UTF-8 encoding scheme, and Python programming skills to validate whether a given dataset represents a valid UTF-8 encoding. Here’s a list of concepts and resources that will be helpful:

## Concepts Needed

### Bitwise Operations in Python

Understanding how to manipulate bits in Python, including operations like AND (`&`), OR (`|`), XOR (`^`), NOT (`~`), shifts (`<<`, `>>`).

#### Example:

```python
a = 0b1010  # 10 in binary
b = 0b1100  # 12 in binary

# AND operation
print(bin(a & b))  # Output: 0b1000

# OR operation
print(bin(a | b))  # Output: 0b1110

# XOR operation
print(bin(a ^ b))  # Output: 0b0110

# NOT operation
print(bin(~a))  # Output: -0b1011 (two's complement representation)

# Left shift
print(bin(a << 2))  # Output: 0b101000

# Right shift
print(bin(a >> 2))  # Output: 0b10
```

### UTF-8 Encoding Scheme

Familiarity with the UTF-8 encoding rules, including how characters are encoded into one or more bytes. Understanding the patterns that represent a valid UTF-8 encoded character.

#### Example:

- A single-byte character (ASCII) in UTF-8: `0xxxxxxx`
- A two-byte character in UTF-8: `110xxxxx 10xxxxxx`
- A three-byte character in UTF-8: `1110xxxx 10xxxxxx 10xxxxxx`
- A four-byte character in UTF-8: `11110xxx 10xxxxxx 10xxxxxx 10xxxxxx`

### Data Representation

How to represent and work with data at the byte level. Handling the least significant bits (LSB) of integers to simulate byte data.

#### Example:

```python
byte_data = [0b11000010, 0b10100010]  # Represents the character '¢' in UTF-8
```

### List Manipulation in Python

Iterating through lists, accessing list elements, and understanding list comprehensions.

#### Example:

```python
data = [1, 2, 3, 4]

# Iterating through list
for item in data:
    print(item)

# Accessing list elements
print(data[0])  # Output: 1

# List comprehension
squared = [x ** 2 for x in data]
print(squared)  # Output: [1, 4, 9, 16]
```

### Boolean Logic

Applying logical operations to make decisions within the program.

#### Example:

```python
a = True
b = False

# AND operation
print(a and b)  # Output: False

# OR operation
print(a or b)  # Output: True

# NOT operation
print(not a)  # Output: False
```

By studying these concepts and utilizing the resources provided, you will be equipped to tackle the UTF-8 validation project, effectively applying bitwise operations and logical reasoning to determine the validity of UTF-8 encoded data.

## Resources

- [Python Bitwise Operators](https://docs.python.org/3/library/stdtypes.html#bitwise-operations-on-integer-types)
- [UTF-8 Wikipedia](https://en.wikipedia.org/wiki/UTF-8)
- [Characters, Symbols, and the Unicode Miracle](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/)
- [Python Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
