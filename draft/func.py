def func():
    ...
    return


func()


def func(arg):
    print(arg)


func(1)


def func(arg, kwarg=None):
    print(arg, kwarg)


func('variable')
func(3.14, True)
func(555, kwarg=True)


def func(*args):
    print(args)


func(1, 2, 4, 5, 6)


def func(**kwargs):
    print(kwargs)


func(first=1, second=2, third=3)


def func(*, kwarg=None):
    print(kwarg)


try:
    func('var')
except TypeError as e:
    print(e)

func(kwarg='var')

# Zwracanie kilku wartości
def func(variable, *, return_duplicate=False):
    if return_duplicate:
        return variable, variable
    return variable

print(func(1))
print(func(1, return_duplicate=True))

from collections import namedtuple
var = namedtuple('var', ['original', 'duplicate'])




# Rekurencja
def func(iter):
    if not iter:
        return
    iter.pop()
    print(iter)
    return func(iter)


func([1, 2, 3, 4, 5])

# Generator
def gen(iter):
    for i in iter:
        print(i)
        yield i


next(gen([1, 2, 3, 4, 5]))

# Dekorator
def decorator(func):
    def wrapper(*args, **kwargs):
        print('@', func, args, kwargs)
        return func(*args, **kwargs)

    return wrapper


@decorator
def func(arg):
    print(arg)


func(True)

# Context Manager
from contextlib import contextmanager


@contextmanager
def context():
    print("in")
    yield
    print("out")


with context():
    print("...")


# Fajny przykład

formaters = []


def formater(func):
    formaters.append(func)
    return func


@formater
def make_text_uppercase(value):
    value = value.upper()
    return value


@formater
def remove_underscore(value):
    value = value.replace("_", " ")
    return value


@formater
def remove_multi_whitespaces(value):
    value = " ".join(value.split())
    return value


def format(value):
    for formater in formaters:
        value = formater(value)
    return value


print(format("this_is_string"))
print(format("this is_also     string"))
