def func():
    return "text"


print(func)
print(type(func))
print(func())

func = lambda: "text"

print(func)
print(type(func))
print(func())


func = lambda x: x
print(func("text"))


func = lambda x, y: x * y
print(func(3, 2))

# Usage

result = map(lambda x: f"_{x}_", range(10))
print("Map", list(result))

result = filter(lambda x: x % 2, range(10))
print("Filter", list(result))

is_title_string = lambda value: type(value) is str and value[0].isupper()
is_not_empty_list = lambda value: type(value) is list and bool(value)
filters = [is_title_string, is_not_empty_list]


def verify_input(value):
    if any([f(value) for f in filters]):
        print("Good value")
    else:
        print("Bad value")


verify_input("Ham")
verify_input(["Ham"])
verify_input({})

# Bytecode
from dis import dis


def func_def(value):
    return value


func_lambda = lambda value: value

dis(func_def)
dis(func_lambda)

from timeit import timeit

time = timeit("def func(): return True", number=10000)
print(f"{'def':>6} {time}")

time = timeit("func=lambda: True", number=10000)
print(f"{'lambda':>6} {time}")
