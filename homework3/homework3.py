# Homework 3: Functions + Conditionals + Loops

def say_goodbye(name):
    print("Goodbye,", name)


def circle_area(radius):
    pi = 3.14
    area = pi * radius * radius
    print("The area of the circle is:", area)


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def min_max_temperatures(readings):
    return (min(readings), max(readings))


def is_weekend(day_number):
    if day_number == 6 or day_number == 7:
        return True
    else:
        return False


def fuel_efficiency(distance, fuel_used):
    return distance / fuel_used


def secret_code(number):
    last_digit = number % 10
    remaining_digits = number // 10

    temp = remaining_digits
    digit_count = 0
    while temp > 0:
        temp = temp // 10
        digit_count += 1

    return last_digit * (10 ** digit_count) + remaining_digits


def power(x, y):
    result = 1
    for _ in range(y):
        result *= x
    return result


def find_min_for(numbers):
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum


def find_max_for(numbers):
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum


def find_min_while(numbers):
    index = 0
    minimum = numbers[0]
    while index < len(numbers):
        if numbers[index] < minimum:
            minimum = numbers[index]
        index += 1
    return minimum


def find_max_while(numbers):
    index = 0
    maximum = numbers[0]
    while index < len(numbers):
        if numbers[index] > maximum:
            maximum = numbers[index]
        index += 1
    return maximum


def sum_of_digits(number):
    total = 0
    while number > 0:
        total += number % 10
        number = number // 10
    return total


if __name__ == "__main__":
    x = 2
    y = 3
    result = power(x, y)
    print(f"The result of power with x = {x} and y = {y} is {result}.")
