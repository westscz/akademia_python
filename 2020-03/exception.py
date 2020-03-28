"""
Article: https://akademiapython.pl/o-obsludze-wyjatkow-i-wyjatkach-slow-kilka/
"""

# 1/0

try:
    1 / 0
except ZeroDivisionError:
    print("Exception occurred")

try:
    1 / 0
except ZeroDivisionError as e:
    print(dir(e))
    print(f"Exception {type(e).__name__}({e}) occurred")

try:
    1 / 2
except ZeroDivisionError:
    print("Exception occurred")
else:
    print("No exception")

try:
    1 / 0
except ZeroDivisionError:
    print("Exception occurred")
else:
    print("No exception")
finally:
    print("Exit")

try:
    None / None
except ZeroDivisionError as e:
    print(f"Exception {type(e)}")
except TypeError as e:
    print(f"Exception {type(e)}")


try:
    1 / 0
except Exception as e:
    print(f"Catch all exceptions {type(e)}")
except ZeroDivisionError as e:
    print(f"Exception {type(e)}")
except TypeError as e:
    print(f"Exception {type(e)}")

print("Some code")
raise LookupError("This code is dangerous!")


class CustomException(Exception):
    """Raised when needed"""


# raise CustomException


class LibraryException(Exception):
    """Base exception for all exceptions in library"""


class CustomException(LibraryException):
    """Raised when needed"""


try:
    raise CustomException
except LibraryException as e:
    print(f"Library exception handled {type(e)}")

try:
    something()
except Exception:
    pass
