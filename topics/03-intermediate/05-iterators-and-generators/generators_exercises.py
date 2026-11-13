"""Iterators and generators: producing values one at a time, on demand.

Implement each one so the tests in test_generators_exercises.py pass.
Run them with:  pytest topics/03-intermediate/05-iterators-and-generators

A generator is a function that uses `yield` instead of `return`. It hands
back one value, pauses, and carries on from the same place when asked for
the next. Nothing is worked out until something asks for it, which is why
a generator can describe a sequence that never ends.

Before you start, predict all three results, then run them:
    >>> squares = (n * n for n in range(4))
    >>> list(squares)
    >>> list(squares)
"""

from collections.abc import Iterable, Iterator


def countdown_from(start: int) -> Iterator[int]:
    """Yield start, start - 1, ... down to 1.

    >>> list(countdown_from(3))
    [3, 2, 1]
    """
    raise NotImplementedError


def evens(numbers: Iterable[int]) -> Iterator[int]:
    """Yield only the even numbers, in order.

    numbers might never end, so don't try to build a list of it first.

    >>> list(evens([1, 2, 3, 4]))
    [2, 4]
    """
    raise NotImplementedError


def take(iterable: Iterable, count: int) -> list:
    """Return the first count items as a list.

    If there are fewer than count items, return them all. Don't take more
    from the iterable than you need: it might be endless, and whoever
    passed it in may want the rest.

    >>> take("abcdef", 2)
    ['a', 'b']
    """
    raise NotImplementedError


def fibonacci() -> Iterator[int]:
    """Yield the Fibonacci numbers for ever: 0, 1, 1, 2, 3, 5, 8, ...

    Each number is the sum of the two before it. An endless loop is
    correct here, because the caller decides when to stop asking.

    >>> take(fibonacci(), 6)
    [0, 1, 1, 2, 3, 5]
    """
    raise NotImplementedError


def non_blank_lines(lines: Iterable[str]) -> Iterator[str]:
    """Yield each line with surrounding whitespace removed, skipping blanks.

    This is how large files are processed: a line at a time, never all
    in memory at once.

    >>> list(non_blank_lines(["  one ", "", "   ", "two"]))
    ['one', 'two']
    """
    raise NotImplementedError


class Countdown:
    """An iterator written by hand, without yield.

    Countdown(3) produces 3, 2, 1 and then stops. A for loop works with
    any object that follows the iterator protocol:

    - __iter__() returns the iterator (here, the object itself)
    - __next__() returns the next value, or raises StopIteration when
      there are none left

    >>> list(Countdown(3))
    [3, 2, 1]
    """

    def __init__(self, start: int) -> None:
        raise NotImplementedError


def flatten(nested: list) -> Iterator:
    """Yield every value from lists nested to any depth. (Stretch)

    Anything that isn't a list is yielded as it is, including strings.
    A generator can hand over to another generator with `yield from`.

    >>> list(flatten([1, [2, [3, 4]], 5]))
    [1, 2, 3, 4, 5]
    """
    raise NotImplementedError
