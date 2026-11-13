"""Type annotations: saying what goes into a function and what comes out.

Run the tests with:  pytest topics/02-fundamentals/11-type-annotations

These stubs are different from the other topics: the annotations are
missing, and adding them is part of the exercise. For each function:

1. Add an annotation to every parameter and to the return value.
2. Implement the function.

The tests check both. Each docstring tells you the exact types to use.
Python never enforces annotations when your code runs. They are there for
readers, for your IDE and for type checkers.
"""

from typing import TypedDict


def add_tax(price, rate):
    """Return price with tax added, e.g. a rate of 0.2 adds 20%.

    Types: price and rate are floats. Returns a float.

    >>> add_tax(100.0, 0.2)
    120.0
    """
    raise NotImplementedError


def shout_all(words):
    """Return every word in uppercase.

    Types: takes a list of strings. Returns a list of strings.

    >>> shout_all(["hi", "there"])
    ['HI', 'THERE']
    """
    raise NotImplementedError


def tally(items):
    """Count how many times each item appears.

    Types: takes a list of strings. Returns a dict that maps each string
    to an int.

    >>> tally(["a", "b", "a"])
    {'a': 2, 'b': 1}
    """
    raise NotImplementedError


def find_age(ages, name):
    """Return the age stored for name, or None if the name isn't there.

    Types: ages is a dict that maps strings to ints, and name is a string.
    The return value is either an int or None. Find out how to write
    "one type or another" in an annotation.

    >>> find_age({"ada": 36}, "ada")
    36
    """
    raise NotImplementedError


def apply_to_all(func, numbers):
    """Call func on every number and return the results as a list.

    Types: func is a function that takes one int and returns an int.
    Look up Callable in collections.abc. numbers is a list of ints, and
    so is the return value.

    >>> apply_to_all(abs, [-1, 2, -3])
    [1, 2, 3]
    """
    raise NotImplementedError


class Movie(TypedDict):
    """A dict that describes a film.

    A TypedDict is an ordinary dict at runtime. It tells readers and type
    checkers which keys the dict has, and the type of each value.

    Give it two keys: title (a string) and year (an int).
    """


def describe_movie(movie):
    """Return the film's title followed by its year in brackets.

    Types: takes a Movie. Returns a string.

    >>> describe_movie({"title": "Alien", "year": 1979})
    'Alien (1979)'
    """
    raise NotImplementedError


def first_or(items, default):
    """Return the first item, or default if the list is empty. (Stretch)

    Types: this works for a list of anything, but default and the return
    value must be the same type as the items in the list. Annotations
    such as list[int] can't say that, so make the function generic with a
    type parameter: read about `def name[T](...)` syntax.

    >>> first_or([4, 5], 0)
    4
    >>> first_or([], "none")
    'none'
    """
    raise NotImplementedError
