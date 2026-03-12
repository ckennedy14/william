# Homework 4
# Lists + Dictionaries

foods = ["pizza", "tacos", "sushi", "burger", "pasta"]
print(foods[1])
print(foods[-1])
foods.append("ramen")
foods.insert(0, "apple")
del foods[2]
print(len(foods))
for food in foods:
    print(food.upper())
new_list = [foods[0], foods[-1]]
print(new_list)
if "potato" in foods:
    print("A potato!")
else:
    print("No potato!")
foods = ["pizza", "tacos", "sushi", "burger", "pasta"]

print(foods[1])
print(foods[-1])

foods.append("ramen")
foods.insert(0, "apple")
del foods[2]

print(len(foods))

for food in foods:
    print(food.upper())

new_list = [foods[0], foods[-1]]
print(new_list)

if "potato" in foods:
    print("A potato!")
else:
    print("No potato!")

numbers = list(range(21))
print(numbers)

def get_first_15(numbers):
    return numbers[:15]

def get_every_5th(lst):
    return lst[::5]

def reverse_and_stride(lst):
    reversed_list = lst[::-1]
    return reversed_list[::3]

step1 = get_first_15(numbers)
step2 = get_every_5th(step1)
step3 = reverse_and_stride(step2)

print(step1)
print(step2)
print(step3)
numbers_nested = [
[1,2,3],
[4,5,6],
[7,8,9]
]

print(numbers_nested[2])
print(numbers_nested[1][1])

numbers_nested.append([10,11,12])
print(numbers_nested)

def sum_nested(lst):
    total = 0
    for row in lst:
        for num in row:
            total += num
    return total

print(sum_nested(numbers_nested))


def create_grid():
    grid = []
    num = 1
    for i in range(5):
        row = []
        for j in range(5):
            row.append(num)
            num += 1
        grid.append(row)
    return grid

grid = create_grid()
print(grid)


def replace_multiples_of_three(lst):
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] % 3 == 0:
                lst[i][j] = "?"
    return lst

grid = replace_multiples_of_three(grid)
print(grid)


def sum_without_q(lst):
    total = 0
    for row in lst:
        for val in row:
            if val != "?":
                total += val
    return total

print(sum_without_q(grid))


ages = {
"Katie": 30,
"Mariam": 42,
"Safia": 25,
"Mira": 48
}

print(ages["Katie"])

ages["Mira"] = 100
ages["Milana"] = 52
del ages["Mariam"]

for name, age in ages.items():
    print(name, age)



"""
Error: SyntaxError: invalid syntax

I originally forgot the colon after the for loop.
Example: for food in foods
I fixed it by adding the colon: for food in foods:
"""

"""
Error: IndexError: list index out of range

I tried to access an index that didn't exist in the list.
I fixed it by using the correct index within the list length.
"""

"""
Error: TypeError: unsupported operand type

I tried to add a string to an integer.
I fixed it by making sure only numbers were added in the sum function.
"""

print(reverse_and_stride([1,2,3,4,5,6,7,8,9,10]))
