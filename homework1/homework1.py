# File: homework1.py
# --- Variables and Data Types ---
a = 10
print(a)
print(type(a))  # a is an integer

b = 1.5
print(b)
print(type(b))  # float

c = 3j
print(c)
print(type(c))  # complex

d = "hello"
print(d)
print(type(d))  # string

e = [1, 2, 3]
print(e)
print(type(e))  # list

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f))  # dictionary

g = (1, 2)
print(g)
print(type(g))  # tuple

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h))  # list

i = True
print(i)
print(type(i))  # boolean

j = None
print(j)
print(type(j))  # NoneType

k = [True, "blue", 12]
print(k)
print(type(k))  # list with mixed types

l = str(14)
print(l)
print(type(l))  # string, because str() converts to text

m = 1e4
print(m)
print(type(m))  # float, scientific notation

# --- Booleans ---
print(10 > 9)             # True, 10 is greater than 9
print(10 == 9)            # False, 10 is not equal to 9
print(10 <= 9)            # False, 10 is not less than or equal to 9
print(bool("abc"))         # True, non-empty string is True
print(bool(123))           # True, non-zero number is True
print(bool(["apple", "cherry", "banana"]))  # True, non-empty list
print(bool(True))          # True
print(bool(False))         # False
print(bool(0))             # False, 0 is considered False
print(bool(""))            # False, empty string is False
print(bool(" "))           # True, string with space is non-empty
print(bool(()))            # False, empty tuple
print(bool([]))            # False, empty list
print(bool({}))            # False, empty dictionary
print(bool(True and False))  # False
print(bool(True and True))   # True
print(bool(False and False)) # False
print(bool(True or False))   # True
print(bool(True or True))    # True
print(bool(False or False))  # False
print(bool(not(False)))      # True
print(bool(not(True)))       # False

# --- Operators ---
# --- Arithmetic Operators ---
print(10 + 5)  # 15, addition
print(10 - 5)  # 5, subtraction
print(2 * 4)   # 8, multiplication
print(6 / 3)   # 2.0, division
print(5 % 2)   # 1, remainder
print(3 ** 2)  # 9, exponent
print(15 // 2) # 7, floor division (integer division)
# --- Comparison Operators ---
print(5 == 2)   # False, 5 is not equal to 2
print(10 != 10) # False, 10 is equal to 10
print(2 < 5)    # True, 2 is less than 5
print(12 > 5)   # True, 12 is greater than 5
print(5 <= 6)   # True, 5 is less than or equal to 6
print(1 >= 10)  # False, 1 is not greater than or equal to 10
# --- Assignment Operators ---
x = 5
print(x)    # 5

x += 5
print(x)    # 10, adds 5

x -= 4
print(x)    # 6, subtracts 4

x *= 3
print(x)    # 18, multiplies by 3
# --- Logical Operators ---
# AND
print(True and True)   # True
print(True and False)  # False

# OR
print(True or False)   # True
print(False or False)  # False

# NOT
print(not(True))       # False
print(not(False))      # True

# --- Strings ---
my_string = "hello"

print(my_string)     # Prints the full string: hello
print(my_string[0])  # h, first character
print(my_string[1])  # e, second character
print(my_string[2])  # l, third character
print(my_string[3])  # l, fourth character
print(my_string[4])  # o, fifth character
print(my_string[-1]) # o, last character
print(my_string[1:3]) # el, slice from index 1 up to 3 (not including 3)
print(my_string[0:5:2]) # hlo, slice from index 0 to 4 with step of 2
print(len(my_string))    # 5, length of string
print(my_string + " goodbye") # hello goodbye, string concatenation
print(my_string * 7)     # hellohellohellohellohellohellohello, repetition
# --- f-Strings ---

name = "Oski"
print("Hello, my name is", name)         # Uses commas, prints: Hello, my name is Oski
print(f"Hello, my name is {name}")       # f-string, prints: Hello, my name is Oski
# The first print uses commas to separate text and variables. It automatically adds a space.
# The second print uses an f-string, which allows you to embed variables directly inside the string using {}.
# --- Terminal Commands ---
# cd
# Changes directories. Use it to move from one folder to another
# Example: cd Desktop

# ls
# Lists files and folders in the current directory
# Example: ls

# ls -a
# Lists all files, including hidden files (those starting with .)
# Example: ls -a

# mkdir
# Creates a new directory
# Example: mkdir new_folder

# cat
# Displays the contents of a file
# Example: cat homework1.py

# pwd
# Prints the current directory path
# Example: pwd

# cd ..
# Moves up one directory level
# Example: cd ..

# cd .
# Refers to the current directory
# Example: cd .

# cd ~
# Moves to your home directory
# Example: cd ~

# cp
# Copies a file or folder
# Example: cp file1.txt file2.txt

# mv
# Moves or renames a file or folder
# Example: mv oldname.txt newname.txt

# rm
# Removes a file (be careful!)
# Example: rm unwanted_file.txt

# clear
# Clears the terminal screen
# Example: clear

# grep
# Searches for text in files
# Example: grep "hello" homework1.py
# 1. Three other commands:
# touch - creates an empty file, Example: touch newfile.txt
# rmdir - removes an empty directory, Example: rmdir old_folder
# echo - prints text to the terminal, Example: echo "Hello"

# 2. Difference between ls and ls -a:
# ls lists visible files, ls -a lists all files including hidden ones

# 3. Hidden file:
# A hidden file starts with a dot (.) and is not shown with normal ls

# 4. Three other flags:
# -l (long listing) Example: ls -l
# -h (human readable sizes) Example: ls -lh
# -R (recursive) Example: ls -R
