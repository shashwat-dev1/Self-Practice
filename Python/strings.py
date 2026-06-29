#String : A string is a sequence of characters enclosed in quotes.
# String can be created using ' " ''' """
s= "Hello"
h= 'Hello Shashwat'
a = """Hello this is
multiline string """
w='''This is 
also a multiline string'''
# String is imutable(cannot change individual chars) 
# ordered(index based access) 
# iterable (looping possible)
# supports slicling

##Indexing & Slicling

s= "Hello"
print(s[0]) ## this will give H
print(s[-1]) ## this will give o also 4 will give o

#Slicling
print(s[0:3]) # Hel
## Slicing works as [start:stop:step] stop n-1 like 3 will go till 2nd index
## Step is like skipping eg. Hlo from Hello will be step=2 as it will go on every 2nd step like skipping 1 char
#step -1 can be used in reversing and -2 -3 will do same stepping in reverse
print(s[::2]) 

## Iteration
for char in s:
    print(char)
##Here H,e,l,l,o will be printed as string is iterable
for i, ch in enumerate(s):
    print(i, ch)
#enumerate() transforms the iterable into index + value pairs

#Operations on string

#concat(adding)
print(s+h)
print("Hello"+"Wrorld")

#repetition
print("Hi"*3) #HiHiHi

#membership using in 
print('h' in "hello") #this will give True


# Methods on String

#case conversion
print(s.lower()) #all chars converted into lowercase
print(s.upper())#all chars converted into uppercase
print(s.title()) # 1st char upper rest lower as title like hello world to Hello World both h and w are upper cased now
print(s.capitalize())
print(s.swapcase())


## Trimming / Cleaning
#strip() : Removes whitespaces from leading + trailing 
#lstrip() : Removes whitespaces from leading(left)
#rstrip() : Removes whitespaces from leading(right)
x="    Hello   "
print(x.strip())
print(x.lstrip())
print(x.rstrip())


# Searching
print(s.find("e")) # return index of e
print(s.find("a")) #this will give -1 as not present
print(s.index("e")) # return index of e
#print(s.index("a")) this will give error as not present
print(s.count("l")) # no. of l in string and this is case sensitive


#Replace 
print(s.replace("e", "x")) 
## This replaces e to x as hxllo replace doesn't change in variable we have to 
# reassign again as s = s.replace("e", "x") and that to now creates new string object
# as memory id points in values in python so when new string is created and reassigned
# s's memory id changes not previous string is changed as string is immutable
# the previous Hello as now have no pointer towards it gets automatically garbage collected i.e deleted


## Splitting & Joining

# split() : Splits a string into a list of substrings
w="hello   world"
w.split()  # output as ['hello', 'world']
#Splits on any whitespace
#Ignores extra spaces
x = "hello world python"
print(x.split(" ")) #output as ['hello', 'world', 'python']
#this one Uses " " (space) as the delimiter
# delimiter : A delimiter acts as a boundary marker that tells a program where one value ends and the next begins.
y = "hello   world"
print(y.split(" ")) #output as ['hello', '', '', 'world']
# Multiple spaces -> empty strings included


# Join : Joins a list of strings into one string
print("-".join(["a", "b", "c"])) #output as a-b-c
# here Uses "-" as the separator

#join() works only on iterables of strings so
# "-".join([1, 2, 3])  This will give error rather
"-".join(map(str, [1, 2, 3]))

#map() : map() is a transformation operator.
#It applies a function to every element in an iterable and returns the results.
# like here map is applying str() to every element as str(1),str(2) etc
#converting into string as join works on strings


# Using both join and split
t = "  hello   world  "
result = "-".join(t.split())
print(result) # output as hello-world (canonical normalization pattern)

# Boolean Checks:
s.isalpha() # Checks if all characters are letters (a–z, A–Z)
"Hello".isalpha()   # True
"Hello1".isalpha()  # False
"Hello World".isalpha()  # False (space breaks it)

s.isdigit() # Checks if all characters are digits (0–9)
"123".isdigit()     # True
"12a3".isdigit()    # False
"²".isdigit()       # True (Unicode digit)

s.isalnum() # Checks if all characters are letters OR digits
"Hello123".isalnum()   # True
"Hello 123".isalnum()  # False (space)
"Hello@123".isalnum()  # False (@)

s.isspace() # Checks if string contains only whitespace
"   ".isspace()   # True
" a ".isspace()   # False
"".isspace()      # False

s.startswith("H") # Checks if string begins with given char
"Hello".startswith("H")   # True
"hello".startswith("H")   # False (case-sensitive)

s.endswith("o") # Checks if string ends with given char
"Hello".endswith("o")   # True
"Hello!".endswith("o")  # False


# String Formatting

# f-strings
name = "Shashwat"
age = 21
print(f"My name is {name} and I am {age}") #The f before the string tells Python evaluate expressions inside {}

# format()
"My name is {}".format(name) # .format(name) → inserts value into placeholder
# Multiple values
"My name is {} and I am {}".format(name, age)
#Indexed placeholders
"{0} is {1} years old".format(name, age)
#Named placeholder
"My name is {n} and I am {a}".format(n=name, a=age)
#format control 
pi = 3.14159
"Value: {:.2f}".format(pi) #this will convert it into round off till 2 decimal places by :.2f where f for float and .2 is defining how many decimal places

# Traditional style formatting
print("%s is %d" % (name, age))


#Some adv ops

#Reversing string (Using step we already know ::-1)
s[::-1]

#Palindrome check (Palindrome is string from forward and backward is same like racecar)
s= "racecar"
s == s[::-1]

#Removing duplicate as we already know set have only unique values so we'll use set for this
"".join(set(s))

# Sorting string using sorted() function
"".join(sorted(s))

# Counting frequency using counter method from collections module
from collections import Counter
Counter(s)

#Type casting 
str(123)
int("123")
list("abc")     # ['a','b','c']

#Reverse words while converting it into list
print("hello world".split()[::-1]) # Output as ['world', 'hello']

#Count vowels
sum(1 for ch in s if ch in "aeiou") 
#Counts the number of vowels (a, e, i, o, u) in string s
#For every vowel found it generates 1

#Checking anagram
## Anagram : An anagram is when two strings contain the same characters with the same frequency, but possibly in a different order.
# Eg. "listen"  ↔ "silent" Correct
# Eg. "hello" ↔ "world"   (different letters)

s1 = "listen"
s2 = "silent"
sorted(s1) == sorted(s2) #This is for checking anagram
print(sorted(s1))  # ['e','i','l','n','s','t']
print(sorted(s2))  # ['e','i','l','n','s','t']
print(sorted(s1) == sorted(s2))  # True

# Can also use Counter()
from collections import Counter
Counter(s1) == Counter(s2)
# This will also check anagram with lesser time complexity 
# Time complexity : Counter O(n) vs sorting O(n log n)


# First non-repeating char
print(next(ch for ch in s if s.count(ch) == 1)) ## get the first character in s that appears only once and print it
#next() is a control operator for iterators.
# It retrieves the next item from an iterator.

## Encoding / Decoding
s = "hello"

encoded = s.encode('utf-8')
print(encoded)
# b'hello'

decoded = encoded.decode('utf-8')
print(decoded)
# 'hello'

# Escape sequence
print("Hello\nWorld")    # newline
print("Hello\tWorld")    # tab
print("He said \"Hi\"")  # embedded quotes
print("Backslash \\")

# Raw Strings
path = r"C:\Users\Shashwat\Desktop" #Prevents escape misinterpretation (\n, \t) converts into raw string
regex = r"\d+\.\d+" #Decimal numbers (numbers with a dot)
# \d+   → one or more digits
# \.    → literal dot (.)
# \d+   → one or more digits

# String Comparison (Lexicographical Engine)
# Character-by-character comparison
# Based on Unicode/ASCII values
"apple" < "banana"   # True
"abc" < "abd"        # True
"A" < "a"            # True (ASCII-based)


# Some built in func
s = "python"

len(s)   # 6 Gives length of string
min(s)   # 'h' gives minimum char based on ascii value
max(s)   # 'y' gives maximum char based on ascii value

# Character Encoding
#ord = ordinal (Converts character → integer (Unicode value))
# Refers to the numeric position/value of a character
# In Python → based on Unicode code point
ord('A')   # 65
# eg. ord('₹')   # 8377

# chr = character converts unicode to char
chr(65)    # 'A'


#Advanced Alignment & Formatting
s = "hi"
#width = total length after padding here 10 is width arg
s.center(10)   # '    hi    ' Places text in the middle Spaces added on both sides as total length is 10 chars
s.ljust(10)    # 'hi        ' Aligns text to the left Spaces added on the right
s.rjust(10)    # '        hi' Aligns text to the right Spaces added on the left

#Zero Padding
"42".zfill(5)   # '00042' Fills zero to get width size 

# partition() : Splits the string into exactly 3 parts based on the first occurrence of separator
s = "hello world"
s.partition(" ") # output as ('hello', ' ', 'world')

## Slicing Edge Cases

s = "python"

# Negative start and stop together
print(s[-3:-1])   # 'ho'  -> from 3rd last to 2nd last (stop is n-1 so -1 excluded)

# Negative step with positive bounds (reverses within range)
print(s[4:1:-1])  # 'noh' -> start at index 4 ('n'), move backward to index 2

# Out of bounds slicing does NOT error (just clips to available chars)
print(s[0:100])   # 'python' (no error, stops at end)
# But indexing out of bounds DOES error
# print(s[100])   # IndexError: string index out of range

# Golden rule : Slicing is forgiving, indexing is strict



## More Splitting / Searching Methods

# splitlines() : Splits on line boundaries (\n, \r, \r\n) — better than split("\n")
text = "line1\nline2\nline3"
print(text.splitlines())        # ['line1', 'line2', 'line3']

# rsplit() : Splits from the RIGHT, can limit splits with maxsplit
path = "a/b/c/d"
print(path.rsplit("/", 1))      # ['a/b/c', 'd']  -> only 1 split from right

# rfind() / rindex() : Search from the RIGHT (returns index from left still)
url = "https://site.com/page.html"
print(url.rfind("."))           # index of LAST dot
# rindex() same but raises ValueError if not found (rfind returns -1)

# rpartition() : partition from the RIGHT (uses LAST occurrence of separator)
email = "user.name@domain.com"
print(email.rpartition("."))    # ('user.name@domain', '.', 'com')



## casefold() — stronger than lower()

# casefold() : Aggressive lowercase designed for Unicode matching
# Better than lower() when comparing strings across languages
ss = "Straße"   # German sharp s
print(ss.lower())       # 'straße'   (still has ß)
print(ss.casefold())    # 'strasse'  (ß -> ss, normalized)
# So : casefold() == True for cross-language string comparison, lower() may miss
"STRASSE".casefold() == "Straße".casefold()   # True
"STRASSE".lower()      == "Straße".lower()     # False (ß != ss in lower)



## removeprefix() / removesuffix() (Python 3.9+)

# Safe, fixed-string prefix/suffix removal — DOES NOT strip chars like lstrip does
filename = "report_final.txt"
print(filename.removeprefix("report_"))   # 'final.txt'
print(filename.removesuffix(".txt"))       # 'report_final'

# IMPORTANT difference from lstrip() :
# lstrip removes ALL chars in the set, not a prefix string
"hello".lstrip("he")      # 'llo'  (strips h AND e, not the word "he")
"hello".removeprefix("he") # 'llo' (removes only the literal prefix "he")
# Use removeprefix/removesuffix when you mean "drop this exact prefix"



## expandtabs()

# expandtabs(tabsize=8) : Converts \t to spaces
code = "a\tb\tc"
print(code.expandtabs(4))    # 'a   b   c' (each tab -> 4 spaces)



## maketrans() / translate() — character-level translation

# maketrans() : Builds a translation table (mapping chars -> chars / None for delete)
# translate() : Applies that table to the string
table = str.maketrans("aeiou", "12345")     # a->1, e->2, i->3, o->4, u->5
print("hello world".translate(table))       # 'h2ll4 w4rld'

# Also delete characters : 3rd arg maps chars to None (remove them)
table2 = str.maketrans("", "", "aeiou")     # delete all vowels
print("hello world".translate(table2))      # 'hll wrld'



## The rest of the is* family

"123".isdigit()       # True  -> 0-9 only
"123.45".isdigit()    # False (. not a digit)
"123.45".isdecimal()  # False -> decimal must be all 0-9 chars
"½".isnumeric()       # True  -> numeric includes fractions, superscripts (broadest)
# Broadness : isdecimal < isdigit < isnumeric

"my_var".isidentifier()    # True  -> valid Python variable name
"my var".isidentifier()    # False (space)
"Hello World".istitle()    # True  -> every word starts uppercase
"Hello world".istitle()    # False
"abc".isprintable()        # True
"abc\n".isprintable()      # False (\n is non-printable)



## format_map() — format from a dict without copying

data = {"name": "Shashwat", "age": 21}
print("My name is {name}".format_map(data))   # 'My name is Shashwat'
# Difference from .format(**data) : format_map does NOT unpack the dict (no copy)
# Useful with dict subclasses like defaultdict that generate keys on the fly



## F-string advanced features

name = "Shashwat"
age = 21
pi = 3.14159

# 1. Expression evaluation inside {}
print(f"Sum = {2 + 3}")                  # 'Sum = 5'

# 2. Inline conditional (ternary)
print(f"{'Mr' if age >= 18 else 'Kid'}")  # 'Mr'

# 3. Debug format f"{var=}" (Python 3.8+) — prints name=value
print(f"{name=}")                        # "name='Shashwat'"
print(f"{age=}")                         # "age=21"

# 4. Format specifiers (after the colon)
print(f"{42:>10}")        # '        42'  -> right-align, width 10
print(f"{42:<10}")        # '42        '  -> left-align
print(f"{42:^10}")        # '    42    '  -> center
print(f"{1234567:,.2f}")  # '1,234,567.00' -> comma thousands + 2 decimals
print(f"{255:x}")         # 'ff'   -> hex
print(f"{255:b}")         # '11111111' -> binary
print(f"{255:o}")         # '377'  -> octal
print(f"{0.15:.1%}")      # '15.0%' -> percentage
print(f"{1234567:.2e}")   # '1.23e+06' -> scientific

# 5. Nested f-strings
width = 10
print(f"{f'{name:^{width}}'}")   # centers 'Shashwat' in width 10



## Interning — why "is" can be True for strings

# Interning : CPython caches certain strings (short, identifier-like) so two
# literals with the same value point to the SAME object in memory
a = "hello"
b = "hello"
print(a is b)   # True  -> interned, same object (same memory id)

# But strings with spaces / built at runtime are usually NOT interned
c = "hello world"
d = "hello world"
print(c is d)   # False (usually) -> different objects, same value

# Manual interning
import sys
e = sys.intern("hello world")
f = sys.intern("hello world")
print(e is f)   # True -> now interned, same object

# is vs == :
# == compares VALUE (the characters)
# is compares IDENTITY (same object in memory)
# Rule : use == for string equality, NEVER rely on is unless you explicitly interned



## String vs bytes vs bytearray

# str    : human text, Unicode, IMMUTABLE
# bytes  : raw byte data, IMMUTABLE (b'...' literal)
# bytearray : mutable version of bytes (can modify elements)

text = "hi"
b = text.encode("utf-8")      # str  -> bytes
print(b)                      # b'hi'
print(b.decode("utf-8"))      # bytes -> str  -> 'hi'

ba = bytearray(b"hello")
ba[0] = 74                    # 74 = 'J' (can mutate! bytes can't)
print(ba)                     # bytearray(b'Jello')



## Encoding error handlers

# When encoding to a charset that can't represent a char, pick a strategy:
s = "café"
print(s.encode("ascii", errors="ignore"))    # b'caf'  -> drop bad char
print(s.encode("ascii", errors="replace"))   # b'caf?' -> replace with ?
# errors="strict" (default) -> raises UnicodeEncodeError



## Regular Expressions (re module) — pattern matching on strings

import re

text = "Call 555-1234 or 999-8765"

# re.findall() : returns ALL matches as a list
print(re.findall(r"\d{3}-\d{4}", text))  # ['555-1234', '999-8765']
# \d{3} -> exactly 3 digits, - literal, \d{4} -> exactly 4 digits

# re.search() : first match anywhere (returns Match object or None)
m = re.search(r"(\d{3})-(\d{4})", text)
print(m.group(0))   # '555-1234' (whole match)
print(m.group(1))    # '555' (1st capture group)

# re.match() : match ONLY at the start of string
# re.sub() : replace matches
print(re.sub(r"\d", "X", text))   # 'Call XXX-XXXX or XXX-XXXX'

# re.split() : split by pattern
print(re.split(r"[\s,]+", "a, b,c  d"))  # ['a', 'b', 'c', 'd']

# re.compile() : pre-compile a pattern for reuse (faster in loops)
phone = re.compile(r"\d{3}-\d{4}")
print(phone.findall(text))

# Flags : re.IGNORECASE (case-insensitive), re.DOTALL (. matches \n)



## string.Template — simple $ substitution

from string import Template
t = Template("Hello $name, you are $age")
print(t.substitute(name="Shashwat", age=21))   # 'Hello Shashwat, you are 21'
# safer when user supplies the string (no format() code injection)
# safe_substitute() won't error if a key is missing
print(t.safe_substitute(name="Shashwat"))       # 'Hello Shashwat, you are $age'



## textwrap module — wrap / shorten / indent / dedent

import textwrap
para = "This is a long sentence that we want to wrap nicely."

print(textwrap.wrap(para, width=20))   # list of lines each <=20 chars
print(textwrap.fill(para, width=20))    # joined into one wrapped string
print(textwrap.shorten(para, width=30)) # 'This is a long [...]'
textwrap.indent("line1\nline2", "  ")   # adds '  ' prefix to each line
textwrap.dedent("  a\n  b")             # removes common leading whitespace



## difflib — fuzzy match / similarity between strings

import difflib
# ratio() : similarity score 0.0 (no overlap) to 1.0 (identical)
print(difflib.SequenceMatcher(None, "apple", "snapple").ratio())  # ~0.9
# get_close_matches() : find closest matches from a list
print(difflib.get_close_matches("appel", ["apple", "banana", "grape"]))
# ['apple']



## Implicit string concatenation

# Two string literals next to each other are joined automatically (no + needed)
msg = "Hello " "World"
print(msg)   # 'Hello World'
# Useful for long strings across lines:
long = ("This is a very long string "
        "split across multiple lines "
        "but it becomes one string.")



## List multiplication gotcha (with strings inside)

# Strings are immutable so this is safe:
print(["hi"] * 3)   # ['hi', 'hi', 'hi']  (3 independent string refs, fine)

# But for nested MUTABLE objects it shares references (classic bug):
matrix = [[""] * 3] * 2
matrix[0][0] = "X"
print(matrix)   # [['X', '', ''], ['X', '', '']]  -> both rows changed!
# Fix : use comprehension so each row is a fresh object
matrix = [[""] * 3 for _ in range(2)]
