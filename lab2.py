# Lab work 2 Askarkyzy Arai
# Python Strings
print("Hello")
print('Hello')
# Quotes Inside Quotes
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')
# Assign String to a Variable
a = "Hello"
print(a)
# Multiline Strings
# Example 1
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
# Example 2
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
# Strings are Arrays
a = "Hello, World!"
print(a[1])
# Looping Through a String
for x in "banana":
    print(x)
# String Length
a = "Hello, World!"
print(len(a))
# Check String
# Example 1
txt = "The best things in life are free!"
print("free" in txt)
# Example 2
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")
# Check if NOT
# Example 1
txt = "The best things in life are free!"
print("expensive" not in txt)
# Example 2
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")

# Slicing Strings
# Slicing
b = "Hello, World!"
print(b[2:5])
# Slice From the Start
b = "Hello, World!"
print(b[:5])
# Slice To the End
b = "Hello, World!"
print(b[2:])
# Negative Indexing
b = "Hello, World!"
print(b[-5:-2])

# Modify Strings
# Upper Case
a = "Hello, World!"
print(a.upper())
# Lower Case
a = "Hello, World!"
print(a.lower())
# Remove Whitespace
a = " Hello, World! "
print(a.strip())  # returns "Hello, World!"
# Replace String
a = "Hello, World!"
print(a.replace("H", "J"))
# Split String
a = "Hello, World!"
print(a.split(","))  # returns ['Hello', ' World!']
# String Methods
n = 'Python'
n.capitalize()  # Converts the first character to upper case
n.casefold()  # Converts string into lower case
n.center()  # Returns a centered string
n.count()  # Returns the number of times a specified value occurs in a string
n.encode()  # Returns an encoded version of the string
n.endswith()  # Returns true if the string ends with the specified value
n.expandtabs()  # Sets the tab size of the string
n.find()  # Searches the string for a specified value and returns the position of where it was found
n.format()  # Formats specified values in a string
n.format_map()  # Formats specified values in a string
n.index()  # Searches the string for a specified value and returns the position of where it was found
n.isalnum()  # Returns True if all characters in the string are alphanumeric
n.isascii()  # Returns True if all characters in the string are ascii characters
n.isdecimal()  # Returns True if all characters in the string are decimals
n.isdigit()  # Returns True if all characters in the string are digits
n.isidentifier()  # Returns True if the string is an identifier
n.islower()  # Returns True if all characters in the string are lower case
n.isnumeric()  # Returns True if all characters in the string are numeric
n.isprintable()  # Returns True if all characters in the string are printable
n.isspace()  # Returns True if all characters in the string are whitespaces
n.istitle()  # Returns True if the string follows the rules of a title
n.isupper()  # Returns True if all characters in the string are upper case
n.join()  # Converts the elements of an iterable into a string
n.ljust()  # Returns a left justified version of the string
n.lower()  # Converts a string into lower case
n.lstrip()  # Returns a left trim version of the string
n.maketrans()  # Returns a translation table to be used in translations
n.partition()  # Returns a tuple where the string is parted into three parts
n.replace()  # Returns a string where a specified value is replaced with a specified value
n.rfind()  # Searches the string for a specified value and returns the last position of where it was found
n.rindex()  # Searches the string for a specified value and returns the last position of where it was found
n.rjust()  # Returns a right justified version of the string
n.rpartition()  # Returns a tuple where the string is parted into three parts
n.rsplit()  # Splits the string at the specified separator, and returns a list
n.rstrip()  # Returns a right trim version of the string
n.split()  # Splits the string at the specified separator, and returns a list
n.splitlines()  # Splits the string at line breaks and returns a list
n.startswith()  # Returns true if the string starts with the specified value
n.strip()  # Returns a trimmed version of the string
n.swapcase()  # Swaps cases, lower case becomes upper case and vice versa
n.title()  # Converts the first character of each word to upper case
n.translate()  # Returns a translated string
n.upper()  # Converts a string into upper case
n.zfill()  # Fills the string with a specified number of 0 values at the beginning

# String Concatenation
# Example 1
a = "Hello"
b = "World"
c = a + b
print(c)
# Example 2
a = "Hello"
b = "World"
c = a + " " + b
print(c)
# Format - Strings
# F-Strings
age = 36
txt = f"My name is John, I am {age}"
print(txt)
# Placeholders and Modifiers
# Example 1
price = 59
txt = f"The price is {price} dollars"
print(txt)
# Example 2
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
# Example 3
txt = f"The price is {20 * 59} dollars"
print(txt)

# Escape Characters
" \' "  # Single Quote
" \\ "  # Backslash
"\n"  # New Line
"\r"  # Carriage Return
"\t"  # Tab
"\b"  # Backspace
"\f"  # Form Feed
"\ooo"  # Octal value
"\xhh"  # Hex value

# Boolean Values
# Example 1
print(10 > 9)
print(10 == 9)
print(10 < 9)
# Example 2
a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")
# Evaluate Values and Variables
# Example 1
print(bool("Hello"))
print(bool(15))
# Example 2
x = "Hello"
y = 15

print(bool(x))
print(bool(y))
# Most Values are True
'''
Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones.

'''
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
# Some Values are False
# Example 1
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
# Example 2


class myclass():
    def __len__(self):
        return 0


myobj = myclass()
print(bool(myobj))
# Functions can Return a Boolean
# Example 1


def myFunction():
    return True


print(myFunction())
# Example 2


def myFunction():
    return True


if myFunction():
    print("YES!")
else:
    print("NO!")
# Example 3
x = 200
print(isinstance(x, int))


# Operators
'''
Python divides the operators in the following groups:

Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators
'''
# Assignment Operators
' = '
x = 5
x = 5
' += '
x += 3
x = x + 3
' -= '
x -= 3
x = x - 3
' *= '
x *= 3
x = x * 3
' /= '
x /= 3
x = x / 3
' %= '
x %= 3
x = x % 3
' //= '
x //= 3
x = x // 3
' **= '
x **= 3
x = x ** 3
' &=	'
x &= 3
x = x & 3
' |= '
x |= 3
x = x | 3
' ^= '
x ^= 3
x = x ^ 3
' >>= '
x >>= 3
x = x >> 3
' <<= '
x <<= 3
x = x << 3
' := '
print(x := 3)
x = 3
print(x)
# Comparison Operators
' == '
# Equal
x == y
' != '
# Not equal
x != y
' > '
# Greater than
x > y
' < '
# Less than
x < y
' >= '
# Greater than or equal to
x >= y
' <= '
# Less than or equal to
x <= y
# Logical Operators
' and '
# Returns True if both statements are true
x < 5 and x < 10
' or '
# Returns True if one of the statements is true
x < 5 or x < 4
' not	'
# Reverse the result, returns False if the result is true
not (x < 5 and x < 10)
# Identity Operators
' is '
# Returns True if both variables are the same object
x is y
' is not '
# Returns True if both variables are not the same object
x is not y
#  Membership Operators
' in '
# Returns True if a sequence with the specified value is present in the object
x in y
' not  in '
# Returns True if a sequence with the specified value is not present in the object
x not in y
# Bitwise Operators
' & '
' AND '
# Sets each bit to 1 if both bits are 1
x & y
' |	'
' OR '
# Sets each bit to 1 if one of two bits is 1
x | y
' ^ '
' XOR '
# Sets each bit to 1 if only one of two bits is 1
x ^ y
' ~ '
' NOT '
# Inverts all the bits
~x
' << '
'Zero fill left shift'
# Shift left by pushing zeros in from the right and let the leftmost bits fall off
x << 2
' >> '
'Signed right shift'
# Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
x >> 2
# Operator Precedence


# Lists
thislist = ["apple", "banana", "cherry"]
print(thislist)
# Length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
# Data Types
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list1 = ["abc", 34, True, 40, "male"]
# type()
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
# The list() Constructor
# note the double round-brackets
thislist = list(("apple", "banana", "cherry"))
print(thislist)
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
# Access List Items
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
# Negative Indexing
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
# Range of Indexes
# Example 1
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
# Example 2
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
# Example 3
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
# Range of Negative Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
# Check if Item Exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")
# Change List Items
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
# Change a Range of Item Values
# Example 1
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
# Example 2
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
thislist = ["apple", "banana", "cherry"]
# Example 3
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
# Insert Items
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
#  Add List Items
# Append Items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
# Insert Items
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
# Extend List
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
# Add Any Iterable
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
#  Remove List Items
# Remove Specified Item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
# Remove Specified Index
# Example 1
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
# Example 2
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
# Example 3
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
# Example 4
thislist = ["apple", "banana", "cherry"]
del thislist
# Clear the List
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
#  Loop Lists
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

# Loop Through the Index Numbers
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])
# Using a While Loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1
# Looping Using List Comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
#  List Comprehension
# Example 1
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)
# Example 2
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
# The Syntax
# Example 1
newlist = [x for x in fruits if x != "apple"]
# Example 2
newlist = [x for x in fruits]
# Iterable
# Example 1
newlist = [x for x in range(10)]
# Example 2
newlist = [x for x in range(10) if x < 5]
# Expression
# Example 1
newlist = [x.upper() for x in fruits]
# Example 2
newlist = ['hello' for x in fruits]
# Example 3
newlist = [x if x != "banana" else "orange" for x in fruits]
#  Sort Lists
# Sort List Alphanumerically
# Example 1
# Example 1
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
# Example 2
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
# Sort Descending
# Example 1
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)
# Example 2
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print(thislist)
# Customize Sort Function


def myfunc(n):
    return abs(n - 50)


thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)
# Case Insensitive Sort
# Example 1
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
# Example 2
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)
# Reverse Order
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
#  Copy Lists
# Use the copy() method
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
# Use the list() method
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
# Use the slice Operator
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)
#  Join Lists
# Join Two Lists
# Example 1
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
# Example 2
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)

print(list1)
# Example 3
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
#  Methods
list1.append()  # Adds an element at the end of the list
list1.clear()  # Removes all the elements from the list
list1.copy()  # Returns a copy of the list
list1.count()  # Returns the number of elements with the specified value
list1.extend()  # Add the elements of a list (or any iterable), to the end of the current list
list1.index()  # Returns the index of the first element with the specified value
list1.insert()  # Adds an element at the specified position
list1.pop()  # Removes the element at the specified position
list1.remove()  # Removes the item with the specified value
list1.reverse()  # Reverses the order of the list
list1.sort()  # Sorts the list


# Tuples
thistuple = ("apple", "banana", "cherry")
print(thistuple)
# Length
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

thistuple = ("apple",)
print(type(thistuple))
# Create Tuple With One Item
# NOT a tuple
thistuple = ("apple")
print(type(thistuple))
# Data Types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple1 = ("abc", 34, True, 40, "male")
# type()
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

# Access Tuple Items
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
# Negative Indexing
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
# Range of Indexes
# Example 1
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])
# Example 3
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])
# Range of Negative Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
# Check if Item Exists
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")
# Update Tuples
'''
Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
'''
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
# Add Items
# Example 1
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
# Example 2
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)
# Remove Items
# Example 1
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
# Example 2
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple)  # this will raise an error because the tuple no longer exists
# Unpack Tuples
# Example 1
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
# Example 2
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
# Example 3
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)
#  Loop Tuples
# Loop Through a Tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)
# Loop Through the Index Numbers
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])
# Using a While Loop
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1
#   Join Tuples
# Join Two Tuples
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
# Multiply Tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
#  Methods
tuple1.count()  # Returns the number of times a specified value occurs in a tuple
tuple1.index()  # Searches the tuple for a specified value and returns the position of where it was found


# Sets
thisset = {"apple", "banana", "cherry"}
print(thisset)
# Get the Length of a Set
thisset = {"apple", "banana", "cherry"}

print(len(thisset))
# Data Types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set1 = {"abc", 34, True, 40, "male"}
# type()
myset = {"apple", "banana", "cherry"}
print(type(myset))
# The set() Constructor
thisset = set(("apple", "banana", "cherry"))  # note the double round-brackets
print(thisset)
#  Access Set Items
# Example 1
thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)
# Example 2
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)
# Example 3
thisset = {"apple", "banana", "cherry"}

print("banana" not in thisset)
#  Add Set Items
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
# Add Sets
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
# Add Any Iterable
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)
#  Remove Set Items
# Example 1
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
# Example 2
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)
# Example 3
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)
# Example 4
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)
# Example 5
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)
#  Loop Sets
thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)
#  Join Sets
'''
The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates.
'''
# Union
# Example 1
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
# Example 2
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)
# Join Multiple Sets
# Example 1
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)
# Example 2
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 | set4
print(myset)
# Join a Set and a Tuple
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)
# Update
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
# Intersection
# Example 1
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)
# Example
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)
# Example 3
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)
# Example 4
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3)
# Difference
# Example 1
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)
# Example 2
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)
# Example 3
set2 = {"google", "microsoft", "apple"}

set1 = {"apple", "banana", "cherry"}
set1.difference_update(set2)

print(set1)
# Symmetric Differences
# Example 1
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)
# Example 2
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)
# Example 3
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)

set1.add()  # Adds an element to the set
set1.clear()  # Removes all the elements from the set
set1.copy()  # Returns a copy of the set
set1.difference()  # Returns a set containing the difference between two or more sets
# Removes the items in this set that are also included in another, specified set
set1.difference_update()
set1.discard()  # Remove the specified item
set1.intersection()  # Returns a set, that is the intersection of two other sets
# Removes the items in this set that are not present in other, specified set(s)
set1.intersection_update()
set1.isdisjoint()  # Returns whether two sets have a intersection or not
set1.issubset()  # Returns whether another set contains this set or not
# Returns whether all items in this set is present in other, specified set(s)
'<'
set1.issuperset()  # Returns whether this set contains another set or not
# Returns whether all items in other, specified set(s) is present in this set
'>'
set1.pop()  # Removes an element from the set
set1.remove()  # Removes the specified element
# Returns a set with the symmetric differences of two sets
set1.symmetric_difference()
# Inserts the symmetric differences from this set and another
set1.symmetric_difference_update()
set1.union()  # Return a set containing the union of sets
set1.update()  # Update the set with the union of this set and others


#  Dictionaries
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)
# Dictionary Items
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict["brand"])
# Dictionary Length
print(len(thisdict))
# Data Types
thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}
# type()
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(type(thisdict))
# The dict() Constructor
thisdict = dict(name="John", age=36, country="Norway")
print(thisdict)
#  Access Dictionary Items
# Example 1
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict["model"]
# Example 2
x = thisdict.get("model")
# Get Keys
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.keys()

print(x)  # before the change

car["color"] = "white"

print(x)  # after the change
# Get Values
# Example 1
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.values()

print(x)  # before the change

car["year"] = 2020

print(x)  # after the change
# Example 2
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.values()

print(x)  # before the change

car["color"] = "red"

print(x)  # after the change
# Get Items
# Example 1
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.items()

print(x)  # before the change

car["year"] = 2020

print(x)  # after the change
# Example 2
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.items()

print(x)  # before the change

car["color"] = "red"

print(x)  # after the change
# Check if Key Exists
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")
#  Change Dictionary Items
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["year"] = 2018
# Update Dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"year": 2020})
#  Add Dictionary Items
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
# Update Dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"color": "red"})
#   Remove Dictionary Items
# Example 1
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.pop("model")
print(thisdict)
# Example 2
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.popitem()
print(thisdict)
# Example 3
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict["model"]
print(thisdict)
# Example 4
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.clear()
print(thisdict)
#  Loop Dictionaries
# Example 1
'''
Print all key names in the dictionary, one by one:
'''

for x in thisdict:
    print(x)
# Example 2
'''
Print all values in the dictionary, one by one:
'''

for x in thisdict:
    print(thisdict[x])
# Example 3
'''
You can also use the values() method to return values of a dictionary:
'''
for x in thisdict.values():
    print(x)
# Example 4
'''
You can use the keys() method to return the keys of a dictionary:
'''

for x in thisdict.keys():
    print(x)
# Example 5
'''
Loop through both keys and values, by using the items() method:
'''
for x, y in thisdict.items():
    print(x, y)
#  Copy Dictionaries
# Example 1
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = thisdict.copy()
print(mydict)
# Example 2
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = dict(thisdict)
print(mydict)
#  Nested Dictionaries
# Example 1
myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}

# Example 2
child1 = {
    "name": "Emil",
    "year": 2004
}
child2 = {
    "name": "Tobias",
    "year": 2007
}
child3 = {
    "name": "Linus",
    "year": 2011
}

myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}


#  Python If ... Else
'''
Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
'''
a = 33
b = 200
if b > a:
    print("b is greater than a")
# Elif
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
# Else
# Example 1
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")
# Example 2
a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")
# Short Hand If
if a > b:
    print("a is greater than b")
# Short Hand If ... Else
# Example 1
a = 2
b = 330
print("A") if a > b else print("B")
# Example 2
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
# And
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")
# Or
a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")
# Not
a = 33
b = 200
if not a > b:
    print("a is NOT greater than b")
# Nested If
x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
# The pass Statement
a = 33
b = 200

if b > a:
    pass
