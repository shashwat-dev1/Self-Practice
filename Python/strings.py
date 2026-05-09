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