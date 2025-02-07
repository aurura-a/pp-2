'''
Funcyions
'''
# In Python a function is defined using the def keyword


def my_function():
    print("Hello from a function")


my_function()


def my_function(fname):
    print(fname + " Refsnes")


my_function("Emil")
my_function("Tobias")
my_function("Linus")


def my_function(fname, lname):
    print(fname + " " + lname)


my_function("Emil", "Refsnes")


'''
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil")
ERROR BECAUSE NUM OF ARGS WHEN U CALL 
FUNCTION MUST BE THE SAME AS THE NUMBER 
OF ARGS FUNCTION HAS
'''


def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")
# The youngest child is Linus
# If you do not know how many arguments that will be passed into your function, add a *


def my_function(child3, child2, child1):
    print("The youngest child is " + child3)


my_function(child1="Emil", child2="Tobias", child3="Linus")


def my_function(child3, child2, child1):
    print("The youngest child is " + child3)


my_function(child1="Emil", child2="Tobias", child3="Linus")


def my_function(**kid):
    print("His last name is " + kid["lname"])


my_function(fname="Tobias", lname="Refsnes")

'''
If you do not know how many keyword argument
that will be passed into your function, add
 two asterisk: ** before the parameter name in the function definition.
This way the function will receive a dictionary of arguments, 
and can access the items accordingly:
'''


def my_function(country="Norway"):
    print("I am from " + country)


my_function("Sweden")
my_function("India")
my_function()  # If we call the function without argument, it uses the default value
my_function("Brazil")


def my_function(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]

my_function(fruits)


def my_function(x):
    return 5 * x


print(my_function(3))
print(my_function(5))
print(my_function(9))


def myfunction():
    pass


def my_function(x, /):
    print(x)


my_function(3)  # positional arguments


# keyword arguments
def my_function(x):
    print(x)


my_function(x=3)
'''ERROR: But when adding the 
, / you will get an error if you try to send a keyword argument:

def my_function(x, /):
  print(x)
'''

my_function(x=3)


def my_function(*, x):
    print(x)


my_function(x=3)


def my_function(x):
    print(x)


my_function(3)


''' ERROR: with the *, 
you will get an error if you try to send a positional argument:
def my_function(*, x):
  print(x)

my_function(3)
'''


def my_function(a, b, /, *, c, d):
    print(a + b + c + d)


my_function(5, 6, c=7, d=8)


def tri_recursion(k):
    if (k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("Recursion Example Results:")
tri_recursion(6)

'''RECURSION
Now, the recursive calls start returning values and adding them:

tri_recursion(0) returns 0
tri_recursion(1) computes 1 + 0 = 1 and prints 1
tri_recursion(2) computes 2 + 1 = 3 and prints 3
tri_recursion(3) computes 3 + 3 = 6 and prints 6
tri_recursion(4) computes 4 + 6 = 10 and prints 10
tri_recursion(5) computes 5 + 10 = 15 and prints 15
tri_recursion(6) computes 6 + 15 = 21 and prints 21
'''


'''
Lambda
'''
# A lambda function can take any number of arguments,
# but can only have one expression.
# lambda arguments : expression


def x(a): return a + 10


print(x(5))


def x(a, b): return a * b


print(x(5, 6))


def x(a, b, c): return a + b + c


print(x(5, 6, 2))


def myfunc(n):
    return lambda a: a * n


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)

print(mydoubler(11))
# 22=11*2


def myfunc(n):
    return lambda a: a * n


mytripler = myfunc(3)

print(mytripler(11))
# 33


'''
Arrays
'''

cars = ["Ford", "Volvo", "BMW"]

x = cars[0]

cars[0] = "Toyota"

x = len(cars)

for x in cars:
    print(x)

cars.append("Honda")

cars.pop(1)

cars.remove("Volvo")

'''
Method	Description
'''


cars.append()  # Adds an element at the end of the list
cars.clear()  # Removes all the elements from the list
cars.copy()  # Returns a copy of the list
cars.count()  # Returns the number of elements with the specified value
cars.index()  # Returns the index of the first element with the specified value
cars.insert()  # Adds an element at the specified position
cars.pop()  # Removes the element at the specified position
cars.remove()  # Removes the first item with the specified value
cars.reverse()  # Reverses the order of the list
cars.sort()  # Sorts the list


''' 
Classes and objects
'''


class MyClass:
    x = 5


p1 = MyClass()
print(p1.x)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)

print(p1.name)
print(p1.age)

# Note: The __init__() function is called
# automatically every time the class is being used to create a new object.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)

print(p1)

# The __str__() function controls
# what should be returned when the class
# object is represented as a string.

# WITHOUT __str__


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)

print(p1)

# WITH __str__


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"


p1 = Person("John", 36)

print(p1)
# result: John(36)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person("John", 36)
p1.myfunc()

# Note: The self parameter is a reference to
# the current instance of the class, and is used
# to access variables that belong to the class.


# Use the words mysillyobject and abc instead of self:
class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)


p1 = Person("John", 36)
p1.myfunc()

p1.age = 40  # Set the age of p1 to 40:
del p1.age  # Delete the age property from the p1 object
del p1  # Delete the p1 object:


class Person:
    pass


'''
Inheritance
'''
# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

# Use the Person class to create an object, and then execute the printname method:


x = Person("John", "Doe")
x.printname()


class Student(Person):
    pass


x = Student("Mike", "Olsen")
x.printname()

# Note: The child's __init__() function
# overrides the inheritance of the parent's __init__() function.


class Student(Person):
    def __init__(self, fname, lname):
        # add properties etc.

        # To keep the inheritance of the parent's __init__() function,
        # add a call to the parent's __init__() function:


class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)


class Student(Person):
    def __init__(self, fname, lname):
        Person().__init__(self, fname, lname)

# Python also has a super() function that will make the child class
# inherit all the methods and properties from its parent:


class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)


class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2019


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year


x = Student("Mike", "Olsen", 2019)


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname,
              "to the class of", self.graduationyear)


x = Student("Mike", "Olsen", 2024)
x.welcome()

# Welcome Mike Olsen to the class of 2024
