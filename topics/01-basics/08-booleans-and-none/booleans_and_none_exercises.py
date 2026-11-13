"""Booleans and None: truthiness, `and`/`or`, and `is None`.

Implement each function so the tests in test_booleans_and_none_exercises.py
pass. Run them with:  pytest topics/01-basics/08-booleans-and-none

Key idea: "falsy" (0, "", [], {}, None, False) is not the same as None.
"""


def is_blank(text: str | None) -> bool:
    """Return True if text is None, empty, or only whitespace.

    >>> is_blank("   ")
    True
    """
    raise NotImplementedError


def describe(value: object) -> str:
    """Return "none" if value is None, "falsy" if it's any other falsy
    value, and "truthy" otherwise.

    >>> describe(0)
    'falsy'
    """
    raise NotImplementedError


def count_truthy(values: list) -> int:
    """Return how many values are truthy.

    Hint: True and False behave like 1 and 0 in arithmetic.

    >>> count_truthy([0, 1, "", "a", None, [1]])
    3
    """
    raise NotImplementedError


def first_truthy(values: list) -> object:
    """Return the first truthy value, or None if there isn't one.

    >>> first_truthy([0, "", "hello", "world"])
    'hello'
    """
    raise NotImplementedError


def display_name(user: dict[str, str | None]) -> str:
    """Choose what to call a user.

    Use their "nickname" if it's present and non-empty, otherwise their
    "full_name" if present and non-empty, otherwise "Anonymous".
    Keys may be missing, or their values may be None or "".

    >>> display_name({"nickname": "", "full_name": "Ada Lovelace"})
    'Ada Lovelace'
    """
    raise NotImplementedError


def apply_overrides(defaults: dict, overrides: dict) -> dict:
    """Merge user overrides on top of default settings. (Stretch)

    An override of None means "not set", so the default is kept. But other
    falsy values like False, 0 and "" are real choices and must win.
    Keys that only appear in overrides are included (unless None).
    Do not modify either input.

    >>> apply_overrides({"volume": 5, "muted": True}, {"volume": 0, "muted": None})
    {'volume': 0, 'muted': True}
    """
    raise NotImplementedError
