'''
Boolean
'''
print(10 > 9)  # True
print(10 == 9)  # False
print(10 < 9)  # False

a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")
# result b is greater than a

# evaluate string and number
print(bool("Hello"))  # True
print(bool(15))  # True

# evaluate variables
x = "Hello"
y = 15

print(bool(x))  # True
print(bool(y))  # True

"""
Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones.
"""
bool("abc")  # True
bool(123)  # True
bool(["apple", "cherry", "banana"])  # True

# ALL RESULTS ARE False
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


class myclass():
    def __len__(self):
        return 0


myobj = myclass()
print(bool(myobj))  # False


def myFunction():
    return True


print(myFunction())  # True


def myFunction():
    return True


if myFunction():
    print("YES!")
else:
    print("NO!")
# result YES!

x = 200
print(isinstance(x, int))  # True


print(10 + 5)  # 15

'''
Python Arithmetic Operators
Operator	Name			Example
+		Addition			x + y	
-		Subtraction			x - y	
*		Multiplication		x * y	
/		Division			x / y	
%		Modulus				x % y	
**		Exponentiation		x ** y	
//		Floor division		x // y
'''
'''
Python Assignment Operators

Operator	Example			Same As
=			x = 5			x = 5	
+=			x += 3			x = x + 3	
-=			x -= 3			x = x - 3	
*=			x *= 3			x = x * 3	
/=			x /= 3			x = x / 3	
%=			x %= 3			x = x % 3	
//=			x //= 3			x = x // 3	
**=			x **= 3			x = x ** 3	
&=			x &= 3			x = x & 3	
|=			x |= 3			 = x | 3	
^=			x ^= 3			x = x ^ 3	
>>=			x >>= 3			x = x >> 3	
<<=			x <<= 3			x = x << 3	
:=			print(x := 3)	x = 3
							print(x)
'''

'''
Python Assignment Operators

Operator	Example			Same As
=			x = 5			x = 5	
+=			x += 3			x = x + 3	
-=			x -= 3			x = x - 3	
*=			x *= 3			x = x * 3	
/=			x /= 3			x = x / 3	
%=			x %= 3			x = x % 3	
//=			x //= 3			x = x // 3	
**=			x **= 3			x = x ** 3	
&=			x &= 3			x = x & 3	
|=			x |= 3			 = x | 3	
^=			x ^= 3			x = x ^ 3	
>>=			x >>= 3			x = x >> 3	
<<=			x <<= 3			x = x << 3	
:=			print(x := 3)	x = 3
							print(x)
'''

'''
Python Comparison Operators

Operator	Name						Example
==			Equal						x == y	
!=			Not equal					x != y	
>			Greater than				x > y	
<			Less than					x < y	
>=			Greater than or equal to	x >= y	
<=			Less than or equal to		x <= y
'''


print((6 + 3) - (6 + 3))  # 0

print(100 + 5 * 3)  # 115

"""
The precedence order is described in the table below, starting with the highest precedence at the top:

Operator				Description	
()						Parentheses	
**						Exponentiation	
+x  -x  ~x				Unary plus, unary minus, and bitwise NOT	
*  /  //  %				Multiplication, division, floor division, and modulus	
+  -					Addition and subtraction	
<<  >>					Bitwise left and right shifts	
&						Bitwise AND	
^						Bitwise XOR	
|						Bitwise OR	
==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
not						Logical NOT	
and						AND	
or						OR
"""

print(5 + 4 - 7 + 3)  # 5
# Addition + and subtraction - has the same precedence, and therefor we evaluate the expression from left to right


'''
List
'''
# List is ordered, Changeable, Allow Duplicates
thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]


list1 = ["abc", 34, True, 40, "male"]

mylist = ["apple", "banana", "cherry"]
print(type(mylist))  # result list

# note the double round-brackets
thislist = list(("apple", "banana", "cherry"))
print(thislist)

"""
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""

thislist = ["apple", "banana", "cherry"]
print(thislist[1])  # banana

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])  # cherry

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])  # cherry, orange, kiwi

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])  # items from the beginning to, but NOT including, "kiwi":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])  # items from "cherry" to the end:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# from "orange" (-4) to, but NOT including "mango" (-1):
print(thislist[-4:-1])

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")


thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)  # apple, blackcurrant, cherry

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)  # apple, blackcurrant, watermelon, orange, kiwi, mango

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)  # ['apple', 'blackcurrant', 'watermelon', 'cherry']

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)  # ['apple', 'watermelon']

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)  # ['apple', 'banana', 'watermelon', 'cherry']

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)  # ['apple', 'banana', 'cherry', 'orange']

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)  # ['apple', 'orange', 'banana', 'cherry']

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
# ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']
print(thislist)


"""The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

Example
Add elements of a tuple to a list:"""

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)  # ['apple', 'banana', 'cherry', 'kiwi', 'orange']

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")  # remove banana
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)  # remove banana
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop()  # remove last item
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]  # remove apple
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist  # del whole list completely

thislist = ["apple", "banana", "cherry"]
thislist.clear()  # empties whole list but the list still remains
print(thislist)

thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
print(newlist)

# with list comprehension we can change these to one line
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

# Only accept items that are not "apple":
newlist = [x for x in fruits if x != "apple"]


newlist = [x for x in fruits]

newlist = [x for x in range(10)]

newlist = [x for x in range(10) if x < 5]

# ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']
newlist = [x.upper() for x in fruits]

newlist = ['hello' for x in fruits]  # all hello in list

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)  # desc
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)  # desc
print(thislist)


def myfunc(n):
    return abs(n - 50)


# customize your own function by using the keyword argument key = function.
# The function will return a number that will be used to sort the list (the lowest number first):
# Sort the list based on how close the number is to 50:
thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
# ['Kiwi', 'Orange', 'banana', 'cherry'] because sort is case sensitive
thislist.sort()
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)  # case-insensitive
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)

print(list1)


list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

n = []
'''
Method	Description
'''
n.append()  # Adds an element at the end of the list
n.clear()  # Removes all the elements from the list
n.copy()  # Returns a copy of the list
n.count()  # Returns the number of elements with the specified value
n.extend()  # Add the elements of a list (or any iterable), to the end of the current list
n.index()  # Returns the index of the first element with the specified value
n.insert()  # Adds an element at the specified position
n.pop()  # Removes the element at the specified position
n.remove()  # Removes the item with the specified value
n.reverse()  # Reverses the order of the list
n.sort()  # Sorts the list


'''
Tuple
'''
# Tuple: ordered, unchangeable, allow duplicates
thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))


thistuple = ("apple",)  # comma!
print(type(thistuple))

# NOT a tuple
thistuple = ("apple")
print(type(thistuple))


tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

tuple1 = ("abc", 34, True, 40, "male")


mytuple = ("apple", "banana", "cherry")
print(type(mytuple))  # tuple

# note the double round-brackets
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")


x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)


thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)


thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple)  # this will raise an error because the tuple no longer exists

fruits = ("apple", "banana", "cherry")  # packing

(green, yellow, red) = fruits  # unpacking

print(green)
print(yellow)
print(red)
# result apple, banana, cherry


fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
# result apple, banana, ['cherry', 'strawberry', 'raspberry']

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)
# result apple,['mango', 'papaya', 'pineapple'], cherry

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)


thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1


tuple1 = ('a', 'b', 'c')
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)


fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

'''
Method	Description
'''

fruits.count()  # Returns the number of times a specified value occurs in a tuple
fruits.index()  # Searches the tuple for a specified value and returns the position of where it was found


'''
Sets
'''
# Sets are unordered, unchangeable, duplicates are not allowed
thisset = {"apple", "banana", "cherry"}
print(thisset)

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)  # removes last apple because it is duplicate


thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)  # true and 1 considered same value

thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)  # false and zero same


thisset = {"apple", "banana", "cherry"}

print(len(thisset))


set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}


set1 = {"abc", 34, True, 40, "male"}


myset = {"apple", "banana", "cherry"}
print(type(myset))  # set


thisset = set(("apple", "banana", "cherry"))  # note the double round-brackets
print(thisset)


thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)


thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

thisset = {"apple", "banana", "cherry"}

print("banana" not in thisset)


thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)


thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)  # merge two sets


thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)  # set + list

print(thisset)


thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)


thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)


thisset = {"apple", "banana", "cherry"}

x = thisset.pop()  # remove random item

print(x)

print(thisset)


thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)


thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)


thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)


"""
oin Sets
There are several ways to join two or more sets in Python.

The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates.
"""

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2  # | and union are the same
print(set3)


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 | set4
print(myset)


x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)  # & and intersection are the same


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

# The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
set1.intersection_update(set2)

print(set1)


set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)  # True, False, apple

print(set3)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)


'''
Dictionary
'''
# Dictionary is as of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# Changeable, Duplicates are not allowed
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict["brand"])


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
print(thisdict)


print(len(thisdict))


thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}


thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(type(thisdict))  # dict

thisdict = dict(name="John", age=36, country="Norway")
print(thisdict)


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict["model"]


x = thisdict.get("model")


x = thisdict.keys()


car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.keys()

print(x)  # before the change

car["color"] = "white"

print(x)  # after the change


x = thisdict.values()


car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.values()

print(x)  # before the change

car["year"] = 2020

print(x)  # after the change


car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.values()

print(x)  # before the change

car["color"] = "red"

print(x)  # after the change


# The items() method will return each item in a dictionary, as tuples in a list.
x = thisdict.items()

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.items()

print(x)  # before the change

car["year"] = 2020

print(x)  # after the change


car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.items()

print(x)  # before the change

car["color"] = "red"

print(x)  # after the change


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["year"] = 2018


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"year": 2020})


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["color"] = "red"
print(thisdict)


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"color": "red"})


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.pop("model")
print(thisdict)


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.popitem()
print(thisdict)


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict["model"]
print(thisdict)


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict
# this will cause an error because "thisdict" no longer exists.
print(thisdict)


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.clear()
print(thisdict)


for x in thisdict:
    print(x)


for x in thisdict:
    print(thisdict[x])


for x in thisdict.values():
    print(x)


for x in thisdict.keys():
    print(x)


for x, y in thisdict.items():
    print(x, y)


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = thisdict.copy()
print(mydict)


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = dict(thisdict)
print(mydict)


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


print(myfamily["child2"]["name"])


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

for x, obj in myfamily.items():
    print(x)

    for y in obj:
        print(y + ':', obj[y])


"""
child1
name: Emil
year: 2004
child2
name: Tobias
year: 2007
child3
name: Linus
year: 2011
"""


a = 33
b = 200
if b > a:
    print("b is greater than a")


a = 33
b = 200
if b > a:
    print("b is greater than a")  # you will get an error because no whitespace


a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")


a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")


a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")


if a > b:
    print("a is greater than b")


a = 2
b = 330
print("A") if a > b else print("B")


a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")


a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")


a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")


a = 33
b = 200
if not a > b:
    print("a is NOT greater than b")


x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")


a = 33
b = 200

if b > a:
    pass


i = 1
while i < 6:
    print(i)
    i += 1


i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1


i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)


i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")


fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)


for x in "banana":
    print(x)


fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break


fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)


fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)


for x in range(6):
    print(x)


for x in range(2, 6):
    print(x)


for x in range(2, 30, 3):
    print(x)


for x in range(6):
    print(x)
else:
    print("Finally finished!")


for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("Finally finished!")


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)


for x in [0, 1, 2]:
    pass
