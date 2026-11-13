"""Comprehensions and iteration: list/dict/set comprehensions,
enumerate, zip and friends.

Implement each function so the tests in test_iteration_exercises.py pass.
Run them with:  pytest topics/02-fundamentals/09-comprehensions-and-iteration

Try to write the first three as a single comprehension each.
"""


def squares_of_evens(numbers: list[int]) -> list[int]:
    """Return the squares of the even numbers, in their original order.

    >>> squares_of_evens([1, 2, 3, 4])
    [4, 16]
    """
    raise NotImplementedError


def word_lengths(words: list[str]) -> dict[str, int]:
    """Map each word to its length.

    >>> word_lengths(["hi", "there"])
    {'hi': 2, 'there': 5}
    """
    raise NotImplementedError


def first_letters(words: list[str]) -> set[str]:
    """Return the set of lowercase first letters. Skip empty strings.

    >>> sorted(first_letters(["Apple", "avocado", "", "banana"]))
    ['a', 'b']
    """
    raise NotImplementedError


def number_lines(lines: list[str]) -> list[str]:
    """Prefix each line with its line number, starting at 1.

    >>> number_lines(["import os", "print(os.getcwd())"])
    ['1: import os', '2: print(os.getcwd())']
    """
    raise NotImplementedError


def pair_up(names: list[str], scores: list[int]) -> dict[str, int]:
    """Match each name to the score in the same position.

    If the lists are different lengths, raise ValueError rather than
    silently dropping data. (Hint: zip can do this for you.)

    >>> pair_up(["ann", "ben"], [7, 9])
    {'ann': 7, 'ben': 9}
    """
    raise NotImplementedError


def chunk(items: list, size: int) -> list[list]:
    """Split items into lists of at most size items each.

    The last chunk may be shorter. Raise ValueError if size is less than 1.

    >>> chunk([1, 2, 3, 4, 5], 2)
    [[1, 2], [3, 4], [5]]
    """
    raise NotImplementedError


def running_total(numbers: list[int]) -> list[int]:
    """Return the running total at each position. (Stretch)

    >>> running_total([3, 1, 4])
    [3, 4, 8]
    """
    raise NotImplementedError


def transpose(matrix: list[list[int]]) -> list[list[int]]:
    """Swap rows and columns of a rectangular grid. (Stretch)

    >>> transpose([[1, 2, 3], [4, 5, 6]])
    [[1, 4], [2, 5], [3, 6]]
    """
    raise NotImplementedError
