"""Functions: defaults, *args/**kwargs, keyword-only args and closures.

Implement each function so the tests in test_functions_exercises.py pass.
Run them with:  pytest topics/02-fundamentals/07-functions
"""

from collections.abc import Callable


def format_price(amount: float, currency: str = "£") -> str:
    """Format an amount of money to two decimal places.

    Negative amounts put the minus sign before the currency symbol.

    >>> format_price(3.5)
    '£3.50'
    >>> format_price(-2, "$")
    '-$2.00'
    """
    raise NotImplementedError


def clamp(value: float, *, low: float, high: float) -> float:
    """Restrict value to the range low..high (inclusive).

    low and high must be passed by keyword, e.g. clamp(5, low=0, high=3).
    The signature above already enforces this. Work out how.

    >>> clamp(15, low=0, high=10)
    10
    """
    raise NotImplementedError


def build_url(base: str, path: str, **params: str | int) -> str:
    """Join a base URL, a path and optional query parameters.

    There must be exactly one "/" between base and path, however the
    caller wrote them. Query parameters appear in the order given, and
    there is no "?" if there are no parameters.

    >>> build_url("https://api.example.com/", "/users", page=2, sort="name")
    'https://api.example.com/users?page=2&sort=name'
    """
    raise NotImplementedError


def add_tag(tag: str, tags: list[str] | None = None) -> list[str]:
    """Append tag to tags and return the list.

    If tags isn't given, start from a fresh empty list every time.

    >>> add_tag("python")
    ['python']
    """
    raise NotImplementedError


def apply_n_times(func: Callable[[int], int], value: int, n: int) -> int:
    """Call func on value, then on the result, n times in total.

    >>> apply_n_times(lambda x: x * 2, 1, 3)
    8
    """
    raise NotImplementedError


def make_counter() -> Callable[[], int]:
    """Return a function that counts up by one each time it's called.

    Each counter returned by make_counter keeps its own count.

    >>> counter = make_counter()
    >>> counter(), counter(), counter()
    (1, 2, 3)
    """
    raise NotImplementedError


def pipeline(*funcs: Callable) -> Callable:
    """Chain functions together, left to right. (Stretch)

    pipeline(f, g, h)(x) is the same as h(g(f(x))).
    With no functions, the returned function gives back its input unchanged.

    >>> shout = pipeline(str.strip, str.upper, lambda s: s + "!")
    >>> shout("  hello ")
    'HELLO!'
    """
    raise NotImplementedError
