"""Regular expressions: describing patterns in text with the re module.

Implement each function so the tests in test_regex_exercises.py pass.
Run them with:  pytest topics/03-intermediate/07-regular-expressions

Write patterns as raw strings, r"\\d+", so that backslashes reach the re
module untouched. https://regex101.com (set to Python) is useful for
trying a pattern out. Remember that plain string methods are often
enough: reach for a regex when the text has a shape, not a fixed value.
"""


def has_digit(text: str) -> bool:
    """Return True if text contains at least one digit.

    >>> has_digit("room 101")
    True
    """
    raise NotImplementedError


def find_numbers(text: str) -> list[int]:
    """Return every whole number in text, as ints, in order.

    >>> find_numbers("Order 66 has 3 items")
    [66, 3]
    """
    raise NotImplementedError


def is_valid_username(name: str) -> bool:
    """Check a username against the sign-up rules.

    It must be 3 to 16 characters long, start with a letter, and contain
    only letters, digits and underscores. The whole name must match, not
    only part of it.

    >>> is_valid_username("ada_99")
    True
    >>> is_valid_username("9lives")
    False
    """
    raise NotImplementedError


def extract_hashtags(text: str) -> list[str]:
    """Return the hashtags in text, without the "#".

    A hashtag is "#" followed by letters, digits or underscores. A group
    in your pattern lets you capture only the part you want.

    >>> extract_hashtags("Learning #Python with #pytest_tips!")
    ['Python', 'pytest_tips']
    """
    raise NotImplementedError


def parse_time(text: str) -> tuple[int, int, int] | None:
    """Turn "HH:MM:SS" into (hours, minutes, seconds), or None if invalid.

    Each part must be exactly two digits. Hours go up to 23, and minutes
    and seconds up to 59. Let the regex check the shape, then check the
    ranges in Python.

    >>> parse_time("09:15:02")
    (9, 15, 2)
    """
    raise NotImplementedError


def mask_emails(text: str) -> str:
    """Hide the name part of every email address in text.

    Everything before the "@" becomes "***". The rest is kept. The re
    module can replace as well as search, and a replacement can refer
    back to a group.

    >>> mask_emails("Write to ada@example.com today")
    'Write to ***@example.com today'
    """
    raise NotImplementedError


def parse_duration(text: str) -> int:
    """Convert a duration such as "1h30m15s" to a number of seconds. (Stretch)

    Hours, minutes and seconds are each optional, but they must appear in
    that order and at least one must be present. Raise ValueError for
    anything else, including "" and "5m2h".

    >>> parse_duration("1h30m15s")
    5415
    >>> parse_duration("45m")
    2700
    """
    raise NotImplementedError
