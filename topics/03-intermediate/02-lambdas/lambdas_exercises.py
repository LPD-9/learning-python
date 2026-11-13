"""Lambdas: small unnamed functions, mostly used as arguments.

Implement each function so the tests in test_lambdas_exercises.py pass.
Run them with:  pytest topics/03-intermediate/02-lambdas

A lambda is a function written as one expression: `lambda x: x * 2`.
Its main use is the key= argument of sorted, min and max, which says what
to compare. If a lambda needs a name or more than one expression, write
a normal function with def instead.
"""

from collections.abc import Callable


def sort_by_last_letter(words: list[str]) -> list[str]:
    """Return the words sorted by their final letter.

    >>> sort_by_last_letter(["cab", "zoo", "arc"])
    ['cab', 'arc', 'zoo']
    """
    raise NotImplementedError


def sort_by_age(people: list[dict]) -> list[dict]:
    """Return the people sorted from youngest to oldest.

    Each person is a dict with "name" and "age" keys.

    >>> sort_by_age([{"name": "Ada", "age": 36}, {"name": "Bob", "age": 25}])
    [{'name': 'Bob', 'age': 25}, {'name': 'Ada', 'age': 36}]
    """
    raise NotImplementedError


def cheapest(products: list[dict]) -> dict | None:
    """Return the product with the lowest "price", or None for an empty list.

    >>> cheapest([{"name": "pen", "price": 2}, {"name": "ink", "price": 1}])
    {'name': 'ink', 'price': 1}
    """
    raise NotImplementedError


def sort_case_insensitive(words: list[str]) -> list[str]:
    """Return the words in alphabetical order, ignoring upper and lower case.

    A key doesn't have to be a lambda. Any function that takes one item
    works, including methods you already know, such as str.upper.

    >>> sort_case_insensitive(["banana", "Apple", "cherry"])
    ['Apple', 'banana', 'cherry']
    """
    raise NotImplementedError


def sort_versions(versions: list[str]) -> list[str]:
    """Return version numbers such as "1.10.0" in true numeric order.

    Sorting them as text is wrong, because "1.10.0" comes before "1.2.0"
    alphabetically. A key can return a list or tuple, and those compare
    item by item.

    >>> sort_versions(["1.10.0", "1.2.0", "1.9.3"])
    ['1.2.0', '1.9.3', '1.10.0']
    """
    raise NotImplementedError


def calculate(operator: str, a: float, b: float) -> float:
    """Apply "+", "-", "*" or "/" to a and b.

    Don't use if/elif. Build a dict that maps each symbol to a lambda,
    then look the symbol up and call what you find. Raise ValueError for
    a symbol that isn't in the dict.

    >>> calculate("*", 3, 4)
    12
    """
    raise NotImplementedError


def group_by(items: list, key: Callable) -> dict:
    """Group items by whatever key(item) returns. (Stretch)

    This time you're on the other side: you write the function that
    accepts a key, like sorted does. Return a dict that maps each key
    value to a list of the items that produced it, in their original
    order.

    >>> group_by(["apple", "avocado", "banana"], lambda word: word[0])
    {'a': ['apple', 'avocado'], 'b': ['banana']}
    """
    raise NotImplementedError
