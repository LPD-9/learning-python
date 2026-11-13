"""Strings: methods, slicing, formatting and characters.

Implement each function so the tests in test_strings_exercises.py pass.
Run them with:  pytest topics/01-basics/05-strings
"""


def normalise_name(name: str) -> str:
    """Tidy up a person's name typed into a form.

    Strip leading/trailing whitespace, collapse any run of internal
    whitespace to a single space, and capitalise each word.

    >>> normalise_name("  ada   lovelace ")
    'Ada Lovelace'
    """
    raise NotImplementedError


def initials(full_name: str) -> str:
    """Return a person's initials, uppercase, each followed by a dot.

    >>> initials("grace  brewster hopper")
    'G.B.H.'
    """
    raise NotImplementedError


def is_palindrome(text: str) -> bool:
    """Return True if text reads the same forwards and backwards.

    Ignore case and anything that isn't a letter or digit.

    >>> is_palindrome("A man, a plan, a canal: Panama")
    True
    """
    raise NotImplementedError


def truncate(text: str, max_length: int) -> str:
    """Shorten text to at most max_length characters, ending in "...".

    If text already fits, return it unchanged. Otherwise cut it so that
    the result, including the "...", is exactly max_length long.
    You can assume max_length is at least 3.

    >>> truncate("Hello, world", 8)
    'Hello...'
    """
    raise NotImplementedError


def parse_log_line(line: str) -> tuple[str, str, str]:
    """Split a log line into (timestamp, level, message).

    A line looks like: "<date> <time> <LEVEL> <message...>".
    The message may itself contain spaces.

    >>> parse_log_line("2026-10-30 09:15:02 ERROR Disk is full")
    ('2026-10-30 09:15:02', 'ERROR', 'Disk is full')
    """
    raise NotImplementedError


def format_row(cells: list[str], widths: list[int]) -> str:
    """Format one row of a text table.

    Each cell is left-aligned and padded with spaces to its width.
    Cells are separated by " | " and the row starts with "| " and
    ends with " |". (Hint: f-strings can pad for you.)

    >>> format_row(["id", "name"], [4, 6])
    '| id   | name   |'
    """
    raise NotImplementedError


def caesar_shift(text: str, shift: int) -> str:
    """Shift each letter along the alphabet by shift places. (Stretch)

    Letters wrap around ("z" shifted by 1 is "a"), keep their case, and
    anything that isn't an ASCII letter is left unchanged. shift may be
    negative or larger than 26.

    >>> caesar_shift("Hello, World!", 3)
    'Khoor, Zruog!'
    """
    raise NotImplementedError
