"""Classes: bundling data with the functions that work on it.

Implement each class so the tests in test_classes_exercises.py pass.
Run them with:  pytest topics/04-oop/01-classes

A class is a template. Each object made from it (an instance) gets its
own copy of the data. `self` is the instance a method was called on.
"""


class Dog:
    """A dog with a name.

    >>> rex = Dog("Rex")
    >>> rex.name
    'Rex'
    >>> rex.speak()
    'Rex says woof'
    """

    def __init__(self, name: str) -> None:
        raise NotImplementedError

    def speak(self) -> str:
        raise NotImplementedError


class Rectangle:
    """A rectangle with a width and a height, stored as attributes.

    >>> page = Rectangle(3, 4)
    >>> page.area()
    12
    >>> page.perimeter()
    14
    """

    def __init__(self, width: float, height: float) -> None:
        raise NotImplementedError

    def area(self) -> float:
        raise NotImplementedError

    def perimeter(self) -> float:
        raise NotImplementedError


class Tally:
    """A click-counter, like the ones used to count people through a door.

    It stores its count in an attribute called `count`, which begins at
    `start`. Methods can change an object's attributes.

    >>> clicker = Tally()
    >>> clicker.click()
    >>> clicker.click()
    >>> clicker.count
    2
    """

    def __init__(self, start: int = 0) -> None:
        raise NotImplementedError

    def click(self) -> None:
        """Add one to the count."""
        raise NotImplementedError

    def reset(self) -> None:
        """Set the count back to zero."""
        raise NotImplementedError


class Playlist:
    """A named list of songs.

    `name` and `songs` are attributes. `songs` begins as an empty list,
    and every playlist must have its own. Adding a song to one playlist
    must never make it appear in another.

    >>> road_trip = Playlist("Road trip")
    >>> road_trip.add("Jolene")
    >>> road_trip.songs
    ['Jolene']
    """

    def __init__(self, name: str) -> None:
        raise NotImplementedError

    def add(self, song: str) -> None:
        raise NotImplementedError

    def count(self) -> int:
        """Return how many songs are in the playlist."""
        raise NotImplementedError


class BankAccount:
    """A bank account with an `owner` and a `balance`.

    An object should refuse changes that would leave it in a state that
    makes no sense.

    >>> account = BankAccount("Ada", 100)
    >>> account.withdraw(30)
    >>> account.balance
    70
    """

    def __init__(self, owner: str, balance: float = 0) -> None:
        raise NotImplementedError

    def deposit(self, amount: float) -> None:
        """Add amount. Raise ValueError if it is zero or less."""
        raise NotImplementedError

    def withdraw(self, amount: float) -> None:
        """Take amount out.

        Raise ValueError if it is zero or less, or more than the balance.
        """
        raise NotImplementedError


class Employee:
    """An employee with a `name`.

    `company` and `headcount` below are class attributes: one value
    shared by the class and all of its instances. Creating an employee
    must add one to the shared headcount.

    Be careful. `self.headcount += 1` doesn't do what it looks like.
    Work out what it does instead.
    """

    company = "Acme"
    headcount = 0

    def __init__(self, name: str) -> None:
        raise NotImplementedError


class Inventory:
    """Stock levels for a shop. (Stretch)

    Decide for yourself how to store the data. The tests only use the
    methods.

    >>> stock = Inventory()
    >>> stock.add("apple", 5)
    >>> stock.remove("apple", 2)
    >>> stock.quantity_of("apple")
    3
    """

    def __init__(self) -> None:
        raise NotImplementedError

    def add(self, item: str, quantity: int = 1) -> None:
        """Add stock. Raise ValueError if quantity is zero or less."""
        raise NotImplementedError

    def remove(self, item: str, quantity: int = 1) -> None:
        """Take stock away.

        Raise KeyError if the item isn't stocked, and ValueError if there
        aren't enough. An item whose stock reaches zero is no longer
        stocked at all.
        """
        raise NotImplementedError

    def quantity_of(self, item: str) -> int:
        """Return how many of item are in stock, or 0 if it isn't stocked."""
        raise NotImplementedError

    def low_stock(self, threshold: int) -> list[str]:
        """Return the items with fewer than threshold in stock, sorted by name."""
        raise NotImplementedError

    def total_items(self) -> int:
        """Return the number of individual items across all stock."""
        raise NotImplementedError
