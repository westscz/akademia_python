from typing import Iterable, Any

# Comprehensions


def map_func(obj) -> Any:
    return obj


def filter_func(obj) -> bool:
    return bool(obj)


def iterable() -> Iterable:
    return range(-2, 5)


result = []
for obj in iterable():
    if filter_func(obj):
        result.append(map_func(obj))

print(result)

result = [map_func(obj) for obj in iterable() if filter_func(obj)]

print(result)

result = [obj for obj in range(-2, 5) if obj]

# Pre

user_input = "123 52 43 -11 1 9 4 0 23 1 1 -2"
input_iter = user_input.split()

# List

numbers = []
for number in input_iter:
    numbers.append(int(number))

numbers = [int(number) for number in input_iter]
print(numbers)

# Dict

numbers_sign = {}
for number in input_iter:
    numbers_sign[int(number)] = number[0] == "-"

numbers_sign = {int(number): number[0] == "-" for number in input_iter}
print(numbers_sign)

# Set

unique_numbers = set()
for number in input_iter:
    unique_numbers.add(int(number))

unique_numbers = {int(number) for number in input_iter}
print(unique_numbers)

# If

positive_numbers = []
for number in input_iter:
    if int(number) >= 0:
        positive_numbers.append(int(number))

positive_numbers = [int(number) for number in input_iter if int(number) >= 0]
print(positive_numbers)

# If else

positive_numbers = []
for number in input_iter:
    if int(number) >= 0:
        positive_numbers.append(int(number))
    else:
        positive_numbers.append(0 - int(number))

positive_numbers = [
    int(number) if int(number) >= 0 else 0 - int(number) for number in input_iter
]
print(positive_numbers)

## Nested

unique_numbers = set()
for number in input_iter:
    for char in number:
        if char != "-":
            unique_numbers.add(int(char))

unique_numbers = {int(char) for number in input_iter for char in number if char != "-"}
print(unique_numbers)

# Gen exp


def numbers(user_input):
    for number in user_input:
        yield int(number)


print(numbers)
numbers_sum = sum(numbers(input_iter))

numbers = (int(number) for number in input_iter)
print(numbers)
numbers_sum = sum(numbers)

numbers_sum = sum(int(number) for number in input_iter)
