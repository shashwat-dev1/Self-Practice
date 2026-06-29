# Floats : Floating-point numbers represent decimal numbers
# They can represent fractional values
# Note: Floats have precision limitations due to binary representation

## Creating Floats

a = 3.14           # standard decimal notation
b = 0.5            # simple float
c = 1.0            # float equals to integer value but still float type
d = -3.5           # negative float
scientific = 1.5e10  # scientific notation (1.5 * 10^10 = 15,000,000,000)
tiny = 2e-5        # 2 * 10^-5 = 0.00002

## Basic Operations

# Arithmetic operations
a = 3.14
b = 2.5

print(a + b)      # 5.64 (addition)
print(a - b)      # 0.64 (subtraction)
print(a * b)      # 7.85 (multiplication)
print(a / b)      # 1.256 (division)
print(a // b)     # 1.0 (floor division - returns float)
print(a % b)      # 1.14 (modulo)
print(a ** b)     # 17.34... (exponentiation)

## Float Precision Issues

# Floating-point arithmetic can have small errors
a = 0.1
b = 0.2
print(a + b)      # 0.30000000000000004 (not exactly 0.3 due to binary representation)

# Python shows many decimal places, but actual precision is limited
print(f"{a + b:.20f}")  # 0.30000000000000004441

# Why? Computers use binary (base 2), but decimals are base 10
# Some decimal numbers cannot be represented exactly in binary

## Comparing Floats

# Direct comparison can be problematic due to precision
a = 0.1 + 0.2
b = 0.3

print(a == b)  # False! (0.30000000000000004 != 0.3)

# Better approach: use a tolerance/epsilon
epsilon = 1e-10  # acceptable error margin

def floats_equal(a, b, epsilon=1e-10):
    return abs(a - b) < epsilon

print(floats_equal(a, b))  # True

## Converting Floats

# Float to int (truncates toward zero)
print(float(3.9))      # 3.9
print(int(3.9))        # 3
print(int(3.0))        # 3
print(int(-3.9))       # -3

# int() truncates (removes decimal part)
# For rounding, use round()
print(round(3.9))      # 4 (rounds to nearest integer)
print(round(3.4))      # 3

# Int to float
print(int(3) * 1.0)    # 3.0
print(float(3))        # 3.0

# String to float
print(float("3.14"))   # 3.14
print(float("3"))      # 3.0

# Error case
try:
    print(float("abc"))
except ValueError:
    print("Invalid float string")

## Float Functions

# abs
print(abs(-3.14))     # 3.14

# round
print(round(3.6))     # 4
print(round(3.2))     # 3
print(round(3.555, 2))  # 3.56 (rounds half up)

# max/min
print(max(1.1, 2.2, 0.5))  # 2.2
print(min(1.1, 2.2, 0.5))  # 0.5

# pow (power)
print(pow(2, 3))       # 8.0
print(pow(2, 0.5))     # 1.414... (square root)

# math functions
import math

print(math.pi)         # 3.141592653589793
print(math.e)          # 2.718281828459045
print(math.sqrt(16))   # 4.0
print(math.floor(3.9)) # 3
print(math.ceil(3.1))  # 4
print(math.trunc(3.9)) # 3
print(math.log(10))    # 2.302585... (natural log)
print(math.log10(100)) # 2.0 (log base 10)
print(math.exp(1))     # 2.71828... (e^1)

## Special Float Values

# Infinity
print(float('inf'))   # inf
print(float('-inf'))  # -inf
print(float('Infinity'))  # inf

# NaN (Not a Number)
print(float('nan'))   # nan

# Comparison with special values
print(float('inf') > 1000)   # True
print(float('nan') == float('nan'))  # False (always False!)
print(float('inf') > float('nan'))   # True (nan is considered less than everything except itself)

## Checking Float Type

print(type(3.14))         # <class 'float'>
print(isinstance(3.14, float))  # True
print(isinstance(3, float))      # False

## Formatting Floats

# Basic formatting
num = 3.14159
print(f"{num}")          # 3.14159
print(f"{num:.2f}")      # 3.14 (2 decimal places)
print(f"{num:.4f}")      # 3.1416 (4 decimal places)
print(f"{num:.0f}")      # 3 (no decimal places)

# With commas for thousands
print(f"{num:,.2f}")     # 3.14

# Percentages
print(f"{0.75:.1%}")     # 75.0%

# Scientific notation
print(f"{1.5e2}")        # 150.0
print(f"{150:.2e}")      # 1.50e+02

## Integer Division vs Float Division

# Integer division returns integer
print(7 / 2)    # 3.5 (returns float)
print(7 // 2)   # 3 (returns integer)

# For more control, use / and // consistently
# Or use int() if you want integer result

## Fraction Representation

# If you need exact decimal arithmetic, use fractions module
from fractions import Fraction

f = Fraction(1, 3)
print(f)        # 1/3
print(float(f)) # 0.333333...

# Fractions avoid floating-point errors
a = Fraction(1, 10) + Fraction(2, 10)
print(a)        # 3/10
print(float(a)) # 0.3 (exact, no error)

## Floats in Memory

# Memory representation
import sys

print(sys.float_info)  # Shows precision, min, max values

# Precision limits
print(sys.float_info.dig)  # 15 (digits of precision)
print(sys.float_info.max)  # 1.7976931348623157e+308

# This means floats can represent about 15-17 significant digits accurately

## Practical Examples

# Temperature conversion
celsius = 25.0
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")

# Currency conversion
usd_per_eur = 1.08
eur_amount = 100.0
usd_amount = eur_amount * usd_per_eur
print(f"{eur_amount} EUR = {usd_amount:.2f} USD")

# Average calculation
scores = [95.5, 87.3, 92.1, 88.0, 90.5]
average = sum(scores) / len(scores)
print(f"Average: {average:.2f}")

# Rounding to nearest whole number
prices = [19.99, 29.99, 39.99]
rounded_prices = [round(p) for p in prices]
print(rounded_prices)  # [20, 30, 40]

## Comparing Floats in Loops

# Common bug: using == with floats in loops
epsilon = 1e-9

for i in range(10):
    value = 0.1 * i
    if abs(value - 0.3) < epsilon:  # Instead of value == 0.3
        print(f"Found 0.3 at i={i}")

# This works because 0.3 * 10 = 3.0 exactly (or very close)
# But 0.1 + 0.2 != 0.3 as we saw earlier

## Percentages and Grading

total_marks = 500
obtained_marks = 375
percentage = (obtained_marks / total_marks) * 100
print(f"Percentage: {percentage:.1f}%")

# Letter grade
if percentage >= 90:
    grade = 'A'
elif percentage >= 80:
    grade = 'B'
elif percentage >= 70:
    grade = 'C'
elif percentage >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"Grade: {grade}")

## Converting Between Units

# Kilometers to miles
km = 100.0
miles = km * 0.621371
print(f"{km} km = {miles:.2f} miles")

# Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

print(celsius_to_fahrenheit(25))  # 77.0

# Pounds to Kilograms
pounds = 150.0
kilograms = pounds * 0.453592
print(f"{pounds} lbs = {kilograms:.2f} kg")

## Scientific Notation

# Large or small numbers
distance_light_year = 9.461e15  # meters
print(distance_light_year)      # 9.461e+15

speed_light = 2.998e8  # meters per second
time_seconds = 86400  # seconds in a day
distance = speed_light * time_seconds
print(f"Light travels {distance:.2e} meters in a day")

## Using Floats with Random Numbers

import random

# Random float between 0 and 1
print(random.random())  # e.g., 0.742...

# Random float between 0 and 10
print(random.uniform(0, 10))  # e.g., 7.42...

# Random float between 1 and 100
print(random.uniform(1, 100))  # e.g., 47.22...

## Floats in Data Structures

# Floats in lists
numbers = [1.1, 2.2, 3.3, 4.4, 5.5]
print(max(numbers))  # 5.5
print(min(numbers))  # 1.1

# Floats in tuples
point = (3.14, 2.71)  # x, y coordinates
print(point[0])       # 3.14

# Floats in dictionaries
data = {
    'name': 'Alice',
    'score': 95.5,
    'age': 25
}
print(data['score'])  # 95.5

## Scientific Calculations

# Area of a circle
radius = 5.0
area = math.pi * radius ** 2
print(f"Area: {area:.2f}")

# Volume of a sphere
radius = 5.0
volume = (4/3) * math.pi * radius ** 3
print(f"Volume: {volume:.2f}")

# Distance between two points
x1, y1 = 1.0, 2.0
x2, y2 = 4.0, 6.0
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"Distance: {distance:.2f}")

## Formatting for Display

# Fixed precision
price = 19.995
print(f"${price:.2f}")  # $20.00 (rounded)

# Using format() function
print("{:.2f}".format(3.14159))  # 3.14

# Align numbers
print(f"{price:>10.2f}")  #     $20.00 (right-aligned)
print(f"{price:<10.2f}")  # $20.00    (left-aligned)

# Zero padding
print(f"{price:010.2f}")  # 000000020.00

## Floating Point Representation Example

# Understanding binary floating point
x = 0.1
y = 0.2
z = x + y
print(f"{z:.20f}")  # 0.30000000000000004441

# This is not a bug, it's how binary floating point works
# For exact decimal arithmetic, use Decimal or Fraction modules

from decimal import Decimal
d = Decimal('0.1') + Decimal('0.2')
print(d)  # Decimal('0.3') - exact!
