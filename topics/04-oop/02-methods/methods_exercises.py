"""Methods: special methods, class methods and static methods.

Implement each class so the tests in test_methods_exercises.py pass.
Run them with:  pytest topics/04-oop/02-methods

Methods whose names begin and end with two underscores are called by
Python itself. `len(team)` calls `team.__len__()`, and `a == b` calls
`a.__eq__(b)`. Writing them lets your own classes work with Python's
built-in syntax.

These stubs give you only a docstring. Choosing the methods, and looking
up how each one is written, is part of the exercise.
"""


class Point:
    """A point with x and y attributes.

    Printing an object normally gives something like
    <Point object at 0x10e3b2>. Write the special method that gives a
    useful description for developers instead.

    >>> Point(1, 2)
    Point(x=1, y=2)
    """


class Money:
    """An amount of money, stored as a whole number of pence.

    There are two special methods that turn an object into text. One is
    for developers (the previous exercise) and one is for people using
    the program. Write the second one.

    >>> str(Money(350))
    '£3.50'
    """


class Card:
    """A playing card with rank and suit attributes.

    By default two objects are equal only if they are the same object.
    Make two cards equal when their rank and suit match. Comparing a card
    with something that isn't a card must give False, not an error.

    >>> Card("A", "spades") == Card("A", "spades")
    True
    """


class Team:
    """A team, created from a list of member names.

    Make these work:

    >>> team = Team(["ada", "bob"])
    >>> len(team)
    2
    >>> "ada" in team
    True
    """


class Duration:
    """A length of time, stored in a `seconds` attribute.

    Besides the ordinary Duration(90), give it:

    - a class method from_minutes(minutes), a second way to create one
    - a class method from_text(text) that understands "M:SS" such as "1:30"
    - a static method is_valid_text(text), which says whether text is in
      that "M:SS" form. Seconds must be two digits, from 00 to 59.

    >>> Duration.from_minutes(2).seconds
    120
    >>> Duration.from_text("1:30").seconds
    90
    >>> Duration.is_valid_text("1:75")
    False
    """


class Vector:
    """A 2D vector with x and y attributes.

    Make all of these work. Adding something that isn't a Vector should
    end in a TypeError: find out what __add__ is meant to return when it
    can't handle the other value.

    >>> Vector(1, 2) + Vector(3, 4) == Vector(4, 6)
    True
    >>> abs(Vector(3, 4))
    5.0
    """


class Version:
    """A version number such as "1.10.3". (Stretch)

    Versions must compare numerically, so "1.10.0" is greater than
    "1.9.0", and all six comparisons (==, !=, <, <=, >, >=) must work, as
    must sorted(). You don't have to write all six by hand: look in
    functools.

    Equal versions must also count as one item in a set. Defining __eq__
    switches that off, so find out what turns it back on.

    >>> Version("1.10.0") > Version("1.9.0")
    True
    >>> Version("2.0.1")
    Version('2.0.1')
    """
