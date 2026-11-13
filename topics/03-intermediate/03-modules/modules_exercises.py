"""Modules: importing from the standard library, and writing your own.

Implement each function so the tests in test_modules_exercises.py pass.
Run them with:  pytest topics/03-intermediate/03-modules

Each of the first five needs a module from Python's standard library.
The docstring names it. Add the imports at the top of this file.

Exercises 6 and 7 are different: you create a new file of your own.
"""


def circle_circumference(radius: float) -> float:
    """Return the distance around a circle: 2 times pi times the radius.

    Module: math. Don't type pi out by hand.
    """
    raise NotImplementedError


def days_between(start: str, end: str) -> int:
    """Return the number of days from start to end.

    Both are dates written as "YYYY-MM-DD". The result is negative if end
    is before start. Module: datetime.

    >>> days_between("2026-01-01", "2026-01-31")
    30
    """
    raise NotImplementedError


def most_common_word(words: list[str]) -> str | None:
    """Return the word that appears most often, or None for an empty list.

    If several words tie, return the one that appeared first.
    Module: collections. It has a class made for counting.

    >>> most_common_word(["tea", "milk", "tea"])
    'tea'
    """
    raise NotImplementedError


def roll_dice(count: int, seed: int) -> list[int]:
    """Return count random dice rolls, each from 1 to 6.

    The same seed must always give the same rolls. That is how programs
    that use randomness are made testable. Module: random. Create your
    own random.Random(seed) so you don't disturb anyone else's.
    """
    raise NotImplementedError


def top_scorer(json_text: str) -> str:
    """Return the name with the highest score.

    json_text is JSON that maps names to scores. Module: json.

    >>> top_scorer('{"ada": 91, "bob": 78}')
    'ada'
    """
    raise NotImplementedError


def shout_twice(text: str) -> str:
    """Exercise 6: write your own module, then use it here.

    Create a file called my_text_tools.py in this folder. Give it:
    - a constant VERSION set to "1.0"
    - a function shout(text) that returns text in capitals with "!" added

    Then import shout into this file and use it to implement shout_twice.

    >>> shout_twice("hey")
    'HEY! HEY!'

    Exercise 7 (Stretch): make my_text_tools.py runnable as a script.

    Give it a main() function that prints "my_text_tools 1.0", using the
    VERSION constant. Running `python my_text_tools.py` must print that
    line. Importing the module must print nothing. One if statement at
    the bottom of the file does this, and you've used it before.
    """
    raise NotImplementedError
