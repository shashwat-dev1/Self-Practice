# Integers : Integers are whole numbers (positive, negative, and zero)
# Integers are immutable, ordered, and unlimited in size
# Supports arithmetic operations

## Creating Integers

a = 42              # positive integer
b = -10             # negative integer
c = 0               # zero
large_num = 999999999999999999999999999999  # Python handles big integers

## Basic Operations

# Arithmetic operations
print(a + b)        # 32 (addition)
print(a - b)        # 52 (subtraction)
print(a * b)        # -420 (multiplication)
print(a / b)        # -4.2 (division - result is float)
print(a // b)       # -5 (floor division - quotient without decimal)
print(a % b)        # 8 (modulo - remainder)
print(a ** b)       # 42^-10 = very small number (exponentiation)

## Comparison Operators

print(a > b)        # True
print(a == b)       # False
print(a != b)       # True
print(a >= b)       # True
print(a <= b)       # False

## Bitwise Operations

a = 5   # binary: 101
b = 3   # binary: 011

print(a & b)   # 1 (binary: 001) - AND
print(a | b)   # 7 (binary: 111) - OR
print(a ^ b)   # 6 (binary: 110) - XOR
print(~a)      # -6 (binary: -010) - NOT
print(a << 2)  # 20 (binary: 0101 << 2 = 10100) - left shift
print(a >> 2)  # 1 (binary: 0101 >> 2 = 0001) - right shift

## Integer Functions

print(abs(-42))     # 42 - absolute value
print(round(3.6))   # 4 - round to nearest integer
print(round(3.2))   # 3
print(pow(2, 10))   # 1024 - power function (2^10)
print(pow(2, 10, 3)) # 1 - power with modulo (2^10 % 3)
print(max(1, 5, 3, 9, 2)) # 9
print(min(1, 5, 3, 9, 2)) # 1
print(bin(5))       # '0b101' - binary representation
print(hex(10))      # '0xa' - hexadecimal representation
print(oct(8))       # '0o10' - octal representation
print(int("42"))    # 42 - string to integer
int("42", 8)       # 34 - string to int with base 8 (octal)
int("1010", 2)     # 10 - string to int with base 2 (binary)

## Type Conversion

float(42)           # 42.0
bool(42)            # True (0 is False, non-zero is True)
str(42)             # '42'

## Integer Literal Formats

# Decimal (default)
dec = 12345

# Binary (prefix 0b)
binary = 0b1010      # 10

# Octal (prefix 0o)
octal = 0o77         # 63

# Hexadecimal (prefix 0x)
hex_val = 0xFF       # 255

# Underscores for readability (Python 3.6+)
large = 1_000_000_000  # 1000000000

## Practical Examples

# Age calculation
current_year = 2024
birth_year = 1990
age = current_year - birth_year
print(f"I am {age} years old")  # I am 34 years old

# Counting occurrences
digits = "12345678901234567890"
count = digits.count("1")
print(count)  # 2

# Sum of range
print(sum(range(1, 11)))  # 55 (sum of 1 to 10)

# Checking divisibility
number = 20
if number % 2 == 0:
    print("Even number")

# Maximum consecutive ones
# Given binary string "111001111"
s = "111001111"
max_count = 0
current = 0
for char in s:
    if char == '1':
        current += 1
        max_count = max(max_count, current)
    else:
        current = 0
print(max_count)  # 3 (first 3 ones)

## Integer Operations with Division

# Regular division vs floor division
print(7 / 2)   # 3.5 (float)
print(7 // 2)  # 3 (integer division)
print(7 % 2)   # 1 (remainder)

## Floating point vs Integer

# When dividing integers, result becomes float
result = 10 / 3
print(result)       # 3.3333333333333335
print(type(result)) # <class 'float'>

# Use // for integer division
result = 10 // 3
print(result)       # 3

## Arithmetic with Modulo

# Use % for finding remainder
# Common uses:
# 1. Checking even/odd
print(10 % 2)   # 0 (even)
print(11 % 2)   # 1 (odd)

# 2. Finding modulus (clock arithmetic)
print(10 % 3)   # 1 (10 = 3*3 + 1)

# 3. Reversing number
num = 123
reversed_num = int(str(num)[::-1])
print(reversed_num)  # 321

## Increment and Decrement

# In Python, no ++ or -- operators
count = 0
count += 1      # equivalent to count = count + 1
count -= 1      # equivalent to count = count - 1

## Comparing Large Numbers

a = 10**100  # 1 followed by 100 zeros
b = 10**100
print(a == b)  # True
print(a is b)  # False (but == is what matters for value)

## Bit Manipulation for Flags

# Using integers as bit flags
flags = 0

# Set bit 0
flags |= 1   # flags = 01
# Set bit 1
flags |= 2   # flags = 11
# Set bit 2
flags |= 4   # flags = 111

print(bin(flags))   # 0b111

# Check if bit 1 is set
if flags & 2:
    print("Bit 1 is set")

# Clear bit 1
flags &= ~2   # Clear bit 1

## Hexadecimal Numbers

# Using hex for memory addresses, colors, etc.
color = 0xFF5733  # Red 255, Green 87, Blue 51
print(hex(color))  # 0xff5733

## Using Integers in String Formatting

name = "Alice"
age = 25
print(f"Hello, {name}! You are {age} years old.")

# Format with padding
print(f"{age:03d}")   # 025 (zero-padded to 3 digits)
print(f"{age:>5}")    #   25 (right-aligned in 5 spaces)
print(f"{age:<5}")    # 25   (left-aligned in 5 spaces)
print(f"{age:^5}")    #  25  (centered in 5 spaces)

## Practical: Fibonacci Sequence

def fibonacci(n):
    """Generate first n Fibonacci numbers"""
    a, b = 0, 1
    fib_list = []
    for _ in range(n):
        fib_list.append(a)
        a, b = b, a + b
    return fib_list

print(fibonacci(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

## Factorial

def factorial(n):
    """Calculate factorial of n"""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))   # 120 (5! = 5*4*3*2*1)

## Number System Conversions

# Decimal to other bases
num = 42
print(bin(num))   # '0b101010'
print(oct(num))   # '0o52'
print(hex(num))   # '0x2a'

# Other bases to decimal
print(int('101010', 2))  # 42 (binary)
print(int('52', 8))      # 42 (octal)
print(int('2a', 16))     # 42 (hexadecimal)

## Integer Overflow

# Python handles big integers automatically
large = 10**1000
print(large)  # No overflow!

## Casting Safety

# int() can fail if string is not a valid number
try:
    print(int("abc"))
except ValueError as e:
    print(f"Error: {e}")  # Error: invalid literal for int() with base 10: 'abc'

# Use try-except for safe conversion
user_input = "42"
try:
    number = int(user_input)
    print(f"Converted to: {number}")
except ValueError:
    print("Please enter a valid number")

## Zero Division with Integers

# Regular division by zero
try:
    result = 5 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# Floor division by zero
try:
    result = 5 // 0
except ZeroDivisionError:
    print("Cannot divide by zero")

## Using Integers with Sets and Dictionaries

# Sets of integers
numbers = {1, 2, 3, 4, 5}
print(numbers & {2, 3, 6})  # {2, 3} (intersection)

# Dictionary with integer keys
scores = {
    1: 95,
    2: 87,
    3: 92
}
print(scores[1])  # 95

## Integer vs Float in Storage

# Integers are stored exactly
i = 1_000_000_000_000_000_000_000
print(i == 1e21)  # True (as float)
# But floating-point has precision issues
f = 1e21
print(i == f)     # False (1e21 as float is not exactly the same)
