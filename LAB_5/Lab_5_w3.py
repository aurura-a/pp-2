# RegEx

# Example
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
# Example

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
# Example

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)
# Example

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())
# Example

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)
# Example

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)
# Example

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)
'''
The Match object has properties and methods used to retrieve information about the search, and the result:

.span() returns a tuple containing the start-, and end positions of the match.
.string returns the string passed into the function
.group() returns the part of the string where there was a match
'''
# Example

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)
# Example

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)
# Example

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)  # this will print an object
# Example

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())
# Example

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())
