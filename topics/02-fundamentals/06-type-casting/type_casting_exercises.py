"""Type casting: converting between str, int, float, bool and collections.

Implement each function so the tests in test_type_casting_exercises.py pass.
Run them with:  pytest topics/02-fundamentals/06-type-casting

Before you start, predict what these give, then run them:
    >>> "2" + "3"
    >>> int("2") + int("3")
    >>> bool("False")
"""


def add_number_strings(a: str, b: str) -> int:
    """Add two whole numbers that arrive as text, e.g. from a web form.

    >>> add_number_strings("2", "3")
    5
    """
    raise NotImplementedError


def digits_of(n: int) -> list[int]:
    """Return the digits of a non-negative whole number, as a list of ints.

    >>> digits_of(4071)
    [4, 0, 7, 1]
    """
    raise NotImplementedError


def unique_sorted(items: list[int]) -> list[int]:
    """Return the distinct items, smallest first, as a list.

    >>> unique_sorted([3, 1, 3, 2, 1])
    [1, 2, 3]
    """
    raise NotImplementedError


def to_bool(text: str) -> bool:
    """Convert a yes/no answer typed by a person into a bool.

    "yes", "true", "1" and "on" mean True. "no", "false", "0" and "off"
    mean False. Ignore case and surrounding whitespace. Raise ValueError
    for anything else.

    >>> to_bool(" Yes ")
    True
    >>> to_bool("off")
    False
    """
    raise NotImplementedError


def parse_number(text: str) -> int | float:
    """Convert text to an int if it's a whole number, otherwise to a float.

    Text that isn't a number at all should raise ValueError. Python's own
    converters already do that, so you don't need to raise it yourself.

    >>> parse_number("42")
    42
    >>> parse_number("3.5")
    3.5
    """
    raise NotImplementedError


def cast_row(row: list[str], types: list[type]) -> list:
    """Convert each value in a row of text to the type in the same position.

    This is what happens when you load a CSV file: everything arrives as
    text and has to be converted. Types such as int and float are values
    you can pass around and call, like any function.

    >>> cast_row(["Ada", "36", "91.5"], [str, int, float])
    ['Ada', 36, 91.5]
    """
    raise NotImplementedError


def safe_int(value: object, default: int = 0) -> int:
    """Convert value to an int without ever raising an error. (Stretch)

    - ints are returned as they are
    - floats are cut down to their whole part (12.9 becomes 12)
    - text is converted if it holds a number, including decimals such as
      "12.9" (which becomes 12) and text with spaces around it
    - anything that can't be converted, including None, gives default

    You'll need try/except for this one.

    >>> safe_int(" 12 ")
    12
    >>> safe_int("twelve", default=-1)
    -1
    """
    raise NotImplementedError
