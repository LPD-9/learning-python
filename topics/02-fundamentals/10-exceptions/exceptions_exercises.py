"""Exceptions: try/except, raising errors, chaining and custom exceptions.

Implement each function so the tests in test_exceptions_exercises.py pass.
Run them with:  pytest topics/02-fundamentals/10-exceptions

Catch the most specific exception you can. A bare `except:` hides bugs.
"""


def safe_divide(a: float, b: float) -> float | None:
    """Return a divided by b, or None if b is zero.

    Let Python attempt the division and catch the error it raises.

    >>> safe_divide(10, 4)
    2.5
    """
    raise NotImplementedError


def get_item(items: list, index: int, default: object = None) -> object:
    """Return items[index], or default if there is no such position.

    Negative positions count from the end, as they normally do.

    >>> get_item(["a", "b"], 5, default="?")
    '?'
    """
    raise NotImplementedError


def require_positive(n: float) -> float:
    """Return n unchanged if it's greater than zero.

    Otherwise raise ValueError with the message "must be positive, got N",
    where N is the number that was passed in.

    >>> require_positive(3)
    3
    """
    raise NotImplementedError


def parse_age(text: str) -> int:
    """Convert a person's age from text to an int, checking it's sensible.

    Raise ValueError with the message:
    - "age must be a whole number" if text isn't a whole number
    - "age must be between 0 and 150" if the number is outside that range

    >>> parse_age("42")
    42
    """
    raise NotImplementedError


def convert_all(texts: list[str]) -> tuple[list[int], list[str]]:
    """Convert every text to an int, without letting one bad value stop you.

    Return two lists: the numbers that converted, and the original texts
    that didn't. Both keep their original order.

    >>> convert_all(["1", "x", "3"])
    ([1, 3], ['x'])
    """
    raise NotImplementedError


def read_setting(settings: dict[str, str], key: str) -> str:
    """Return settings[key], with a clearer error when the key is missing.

    If the key is missing, catch the KeyError and raise ValueError with the
    message "missing setting: KEY". Chain the new error to the original
    with `raise ... from ...`, so the traceback shows both.

    >>> read_setting({"host": "localhost"}, "host")
    'localhost'
    """
    raise NotImplementedError


class InsufficientFundsError(Exception):
    """Raised by withdraw() when an account doesn't hold enough money.

    Give it an __init__ that takes the shortfall (how much more money was
    needed), stores it as self.shortfall, and passes a helpful message up
    to Exception.
    """


def withdraw(balance: float, amount: float) -> float:
    """Take amount out of balance and return the new balance. (Stretch)

    - Raise ValueError if amount is zero or less.
    - Raise InsufficientFundsError if amount is more than balance. Its
      shortfall attribute must hold how much more money was needed.

    >>> withdraw(100, 30)
    70
    """
    raise NotImplementedError
