# File Handling
'''
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists
'''
# Syntax
import os
f = open("demofile.txt")
f = open("demofile.txt", "rt")


# Read Files
'''
To open the file, use the built-in open() function.

The open() function returns a file object, which has a read() method for reading the content of the file:
'''
# Example
f = open("demofile.txt", "r")
print(f.read())
# Example
f = open("D:\\myfiles\welcome.txt", "r")
print(f.read())
# Example
f = open("demofile.txt", "r")
print(f.read(5))
# Example
f = open("demofile.txt", "r")
print(f.readline())
# Example
f = open("demofile.txt", "r")
for x in f:
    print(x)
# Example
f = open("demofile.txt", "r")
print(f.readline())
f.close()


# File Write
'''
To write to an existing file, you must add a parameter to the open() function:

"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing content
'''
# Example
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

# open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())
# Example
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

# open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read())
# Create a New File
'''
To create a new file in Python, use the open() method, with one of the following parameters:

"x" - Create - will create a file, returns an error if the file exists

"a" - Append - will create a file if the specified file does not exists

"w" - Write - will create a file if the specified file does not exists
'''


# Delete File
# Example
os.remove("demofile.txt")
# Example
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")
# Example
os.rmdir("myfolder")
