# Python Iterators
'''An iterator is an object that contains a countable number of values.

An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.

Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().
'''
# Example
import json
import math
import datetime
import platform
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
# Example
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
# Example
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
    print(x)
# Example
mystr = "banana"

for x in mystr:
    print(x)
# Example


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
# Example


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)
# Scope
# Example


def myfunc():
    x = 300
    print(x)


myfunc()
# Example


def myfunc():
    x = 300

    def myinnerfunc():
        print(x)
    myinnerfunc()


myfunc()
# Example
x = 300


def myfunc():
    print(x)


myfunc()

print(x)
# Example
x = 300


def myfunc():
    x = 200
    print(x)


myfunc()

print(x)
# Example


def myfunc():
    global x
    x = 300


myfunc()

print(x)
print(x)
# Example


def myfunc1():
    x = "Jane"

    def myfunc2():
        nonlocal x
        x = "hello"
    myfunc2()
    return x


print(myfunc1())
# Modules
'''
Consider a module to be the same as a code library.

A file containing a set of functions you want to include in your application.
'''
# Example


def greeting(name):
    print("Hello, " + name)


# Example
person1 = {
    "name": "John",
    "age": 36,
    "country": "Norway"
}

x = platform.system()
print(x)

x = platform.system()
print(x)
# Example


def greeting(name):
    print("Hello, " + name)


person1 = {
    "name": "John",
    "age": 36,
    "country": "Norway"
}
# Example
x = 300


def myfunc():
    print(x)


myfunc()

print(x)
# Example
x = 300


def myfunc():
    x = 200
    print(x)


myfunc()

print(x)
# Example


def myfunc():
    global x
    x = 300


myfunc()

print(x)
print(x)
# Example


def myfunc1():
    x = "Jane"

    def myfunc2():
        nonlocal x
        x = "hello"
    myfunc2()
    return x


print(myfunc1())
# Modules
'''
Consider a module to be the same as a code library.

A file containing a set of functions you want to include in your application.
'''
# Example


def greeting(name):
    print("Hello, " + name)


# Example
person1 = {
    "name": "John",
    "age": 36,
    "country": "Norway"
}

x = platform.system()
print(x)

x = platform.system()
print(x)
# Example


def greeting(name):
    print("Hello, " + name)


person1 = {
    "name": "John",
    "age": 36,
    "country": "Norway"
}
# Datetime
# Example

x = datetime.datetime.now()
print(x)
# Example

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))
# Example

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))
# Math
# Example
y = max(5, 10, 25)
x = min(5, 10, 25)

print(x)
print(y)
# Example
x = pow(4, 3)

print(x)
# Example
x = abs(-7.25)

print(x)
# Example

x = math.sqrt(64)

print(x)
# Example

x = math.ceil(1.4)
y = math.floor(1.4)

print(x)  # returns 2
print(y)  # returns 1
# Example

x = math.pi

print(x)
# JSON
'''
If you have a JSON string, you can parse it by using the json.loads() method.
'''
# Example


# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
'''
If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.
'''

# a Python object (dict):
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
