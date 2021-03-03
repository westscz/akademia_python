"""
Bibliography:

- https://en.wikipedia.org/wiki/List_comprehension

"""

# Comprehension


def map_function(item):
    return item


def filter_function(item):
    return bool(item)


iterable = range(10)

result = []
for variable in iterable:
    if filter_function(variable):
        result.append(map_function(variable))
print(result)

result = [map_function(variable) for variable in iterable if filter_function(variable)]
print(result)

# List

user_input = "1 2 47 92 43 22"

numbers = []
for i in user_input.split():
    numbers.append(int(i))

definition = [True]
t = type(definition)
print(t)

numbers = [int(i) for i in user_input.split(" ")]

# Dict

definition = {"key": 1}
t = type(definition)
print(t)

users = [
    {
        "id": 1,
        "username": "Jaymie-Bousfield",
        "email": "jbousfield0@qq.com",
        "gender": "Male",
        "ip": "129.116.249.144",
    },
    {
        "id": 2,
        "username": "Caleb-Biskupiak",
        "email": "cbiskupiak1@jugem.jp",
        "gender": "Male",
        "ip": "86.56.37.243",
    },
    {
        "id": 3,
        "username": "Brice-Quadling",
        "email": "bquadling2@flavors.me",
        "gender": "Male",
        "ip": "161.249.19.232",
    },
    {
        "id": 4,
        "username": "Dorolice-Seatter",
        "email": "dseatter3@unc.edu",
        "gender": "Female",
        "ip": "240.58.159.255",
    },
]

user_email = {}
for user in users:
    user_email[user["username"]] = user["email"]

user_email = {user["username"]: user["email"] for user in users}
print(user_email)

# Set

definition = {True}
t = type(definition)
print(t)

ips = set()
for user in users:
    ips.add(user["ip"])

ips = {user["ip"] for user in users}
print(ips)

# If

com_domain = []
for user in users:
    if user["email"][-3:] == "com":
        com_domain.append(user["email"])


com_postfix = [user["email"] for user in users if user["email"][-3:] == "com"]
print(com_postfix)


def is_postfix(email, domain):
    return user["email"].rsplit(".")[-1] == domain


com_postfix = [user["email"] for user in users if is_postfix(user["email"], "com")]

# If else TODO

# proper_postfix = {}
# for user in users:
#     if is_postfix(user["email"], "com"):
#         proper_postfix[user['username']] = True
#     else:
#         proper_postfix[user['username']] = False
# print(proper_postfix)

# proper_postfix = [c.lower() if is_postfix(user["email"], "com") else c for user in users]
# print(proper_postfix)

# Nested

values = []
for user in users:
    for key, value in user.items():
        values.append(value)

values = [value for user in users for key, value in user.items()]
print(values)


# Generator

definition = (True,)
t = type(definition)
print(t)


def gen():
    for i in range(10):
        yield i % 2


print(gen())

gen = (i % 2 for i in range(10))
print(gen)

# Use cases

users = [
    {"username": "qwerty", "hash": "fi404m9rf", "is_admin": True},
    {"username": "qwesdty", "hash": "fi404m9rf", "is_admin": False},
    {"username": "qasfdrty", "hash": "fi404m9rf", "is_admin": False},
    {"username": "qwegy", "hash": "fi404m9rf", "is_admin": True},
]

any_admin = any({user["is_admin"] for user in users})
print(any_admin)

admins = [user for user in users if user["is_admin"]]
print(admins)

first_admin = next(user for user in users if user["is_admin"])
print(first_admin)
