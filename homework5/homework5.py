# Vocabulary Review

# Git vs GitHub
# Git tracks changes locally. GitHub stores code online.

# Terminal vs Command Line
# Terminal is the app. Command line is where you type commands.

# Local vs Remote Repository
# Local is on your computer. Remote is on GitHub.

# Version Control
# Tracks file changes over time.

# Staging Area
# Holds changes before commit.

# git add
# Adds files to staging.

# git commit
# Saves changes.

# git push
# Sends changes to GitHub.

# git status
# Shows repo state.

# git pull
# Gets updates from GitHub.

# pwd
# Shows current directory.

# ls
# Lists files.

# cd
# Changes directory.

# nano
# Opens text editor.

# touch
# Creates file.

# mv
# Moves or renames file.

# rm
# Deletes file.

# cat
# Shows file contents.


# Directory Questions

# pwd
# ls
# cd into repo then git pull origin main
# mv homework.py ~/python_decal/judy_decal/homework/
# cd ~/python_decal/judy_decal/homework
# cat homework.py
# git add . then git commit then git push
# git pull then git push
# /Users/judy/Recents


def checkDataType(value):
    return type(value).__name__


def evenOrOdd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


def sumWithLoop(numbers):
    total = 0
    for n in numbers:
        total += n
    return total


def duplicateList(items):
    result = []
    for item in items:
        result.append(item)
        result.append(item)
    return result


def square(num):
    return num * num


print(checkDataType(3.14))
print(evenOrOdd(7))
print(sumWithLoop([1,2,3,4,5]))
print(duplicateList(["a","b","c"]))
print(square(5))
