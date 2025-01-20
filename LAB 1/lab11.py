# Lab work 1 Askarkyzy Arai

import random
import sys
print("Hello, World!")


# Python Version

print(sys.version)

# Python Indentation
if 5 > 2:
    print("Five is greater than two!")
'''
Python will give you an error if you skip the indentation
Syntax Error:

if 5 > 2:
print("Five is greater than two!")
'''

# Creating a Comment
# This is a comment
print("Hello, World!")
print("Hello, World!")  # This is a comment
# print("Hello, World!")
print("Cheers, Mate!")

# Multiline Comments
# This is a comment
# written in
# more than just one line
print("Hello, World!")
"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")


# Variables
# Example 1
x = 5
y = "John"
print(x)
print(y)
# Example 2
x = 4       # x is of type int
x = "Sally"  # x is now of type str
print(x)
# Example 3
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# Get the Type
x = 5
y = "John"
print(type(x))
print(type(y))

# Single or Double Quotes?
x = "John"
# is the same as
x = 'John'

# Case-Sensitive
a = 4
A = "Sally"
# A will not overwrite a


# Variable Names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
'''
Illegal variable names:

2myvar = "John"
my-var = "John"
my var = "John"
'''
# There are several techniques you can use to make them more readable:
# Camel Case
myVariableName = "John"
# Pascal Case
MyVariableName = "John"
# Snake Case
my_variable_name = "John"

# Many Values to Multiple Variables
# Example 1
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
# Example 2
x = y = z = "Orange"
print(x)
print(y)
print(z)
# Example 3. If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking:
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Output Variables
# Example 1
x = "Python is awesome"
print(x)
# Example 2
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
# Example 3
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
# Example 4
x = 5
y = 10
print(x + y)
# Example 5
x = 5
y = "John"
print(x + y)
'''
In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error
'''
# Example 6
x = 5
y = "John"
print(x, y)


# Global Variables
# Example 1
x = "awesome"


def myfunc():
    print("Python is " + x)


myfunc()
# Example 2
x = "awesome"


def myfunc():
    x = "fantastic"
    print("Python is " + x)


myfunc()

print("Python is " + x)
# The global Keyword
# Example 1


def myfunc():
    global x
    x = "fantastic"


myfunc()

print("Python is " + x)
# Example 2
x = "awesome"


def myfunc():
    global x
    x = "fantastic"


myfunc()

print("Python is " + x)


# Python Data Types
# str
x = "Hello World"

# display x:
print(x)

# display the data type of x:
print(type(x))
# int
x = 20

# display x:
print(x)

# display the data type of x:
print(type(x))
# float
x = 20.5

# display x:
print(x)

# display the data type of x:
print(type(x))
# complex
x = 1j

# display x:
print(x)

# display the data type of x:
print(type(x))
# list
x = ["apple", "banana", "cherry"]

# display x:
print(x)

# display the data type of x:
print(type(x))
# tuple
x = ("apple", "banana", "cherry")

# display x:
print(x)

# display the data type of x:
print(type(x))
# range
x = range(6)

# display x:
print(x)

# display the data type of x:
print(type(x))
# dict
x = {"name": "John", "age": 36}

# display x:
print(x)

# display the data type of x:
print(type(x))
# set
x = {"apple", "banana", "cherry"}

# display x:
print(x)

# display the data type of x:
print(type(x))
# bool
x = True

# display x:
print(x)

# display the data type of x:
print(type(x))
# bytes
x = b"Hello"

# display x:
print(x)

# display the data type of x:
print(type(x))
# bytearray
x = bytearray(5)

# display x:
print(x)

# display the data type of x:
print(type(x))
# memoryview
x = memoryview(bytes(5))

# display x:
print(x)

# display the data type of x:
print(type(x))
# NoneType
x = None

# display x:
print(x)

# display the data type of x:
print(type(x))


# Python Numbers
# Example 1
x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(type(x))
print(type(y))
print(type(z))
# Example 2
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))
# Example 3
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))
# Example 4
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))
# Example 5
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

# Type Conversion
x = 1    # int
y = 2.8  # float
z = 1j   # complex

# convert from int to float:
a = float(x)

# convert from float to int:
b = int(y)

# convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# Random Number

print(random.randrange(1, 10))


# Python Casting
# Example 1
x = int(1)   # x will be 1
y = int(2.8)  # y will be 2
z = int("3")  # z will be 3
# Example 2
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2")  # w will be 4.2
# Example 3
x = str("s1")  # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
