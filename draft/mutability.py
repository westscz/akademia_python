type((1).__hash__)
"> <type 'method-wrapper'>"
type((1.42).__hash__)
"> <type 'method-wrapper'>"
type(("str").__hash__)
"> <type 'method-wrapper'>"
type(().__hash__)
"> <type 'method-wrapper'>"

type(([]).__hash__)
"> <type 'NoneType'>"
type(({}).__hash__)
"> <type 'NoneType'>"


class Prototype(object):
    def __init__(self, x):
        self.x = x


print(hash(Prototype(1)))
print(hash(Prototype(2)))
print(hash(Prototype(1)))
"""
275708106
275708106
275708106
"""
print(id(Prototype(1)) / 16)
"""
284584828.0
"""


class Prototype:
    def __init__(self, x):
        self.x = x

    __hash__ = None


# print(hash(Prototype(1)))
"> TypeError: unhashable type: 'Prototype'"


class Prototype:
    def __init__(self, number):
        self.number = number

    def __hash__(self):
        print(f"{self.__class__.__name__}-{self.number}")
        return hash(f"{self.__class__.__name__}-{self.number}")

    def __eq__(self, other):
        return self.number == other.number


d = {}
d[Prototype(1.01)] = 78
d[Prototype(2.51)] = 3

print(d[Prototype(1.01)])
"> 78"

# Hash collections

try:
    {[]: 12}
except TypeError as e:
    print(e)

try:
    {{}}
except TypeError as e:
    print(e)

print({1, 2, 3, False, True, 1.0, 0})

# Hash colission

print(hash(1))
print(hash(True))
print(hash(1.00))
