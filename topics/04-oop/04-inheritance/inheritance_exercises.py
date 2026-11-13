"""Inheritance: building classes on top of other classes.

Implement each class so the tests in test_inheritance_exercises.py pass.
Run them with:  pytest topics/04-oop/04-inheritance

A subclass gets everything its parent has, and can add to it or replace
parts of it. Some classes below are finished and marked "Given". Leave
those alone and write the others.

The classes you write are declared here without a parent. Each docstring
says what the class is a kind of. Adding that parent in brackets after
the class name is the first step of every exercise.

A warning that senior engineers repeat often: inheritance is easy to
overuse. Use it when the subclass really is a kind of the parent. When
one thing merely uses another, give it an attribute that holds the other
object instead. That is called composition, and the last exercise uses it.
"""

from abc import ABC, abstractmethod  # noqa: F401  (you'll need these)


class Animal:
    """Given. An animal that can describe the sound it makes."""

    def __init__(self, name: str) -> None:
        self.name = name

    def sound(self) -> str:
        raise NotImplementedError("each kind of animal provides its own sound")

    def describe(self) -> str:
        return f"{self.name} says {self.sound()}"


class Dog:
    """A dog, which is a kind of Animal. Its sound is "Woof".

    Don't rewrite describe(): it is inherited.

    >>> Dog("Rex").describe()
    'Rex says Woof'
    """


class Cat:
    """A cat, which is a kind of Animal. Its sound is "Meow"."""


class Employee:
    """Given. Someone who works for the company."""

    def __init__(self, name: str, salary: int) -> None:
        self.name = name
        self.salary = salary

    def describe(self) -> str:
        return f"{self.name} (£{self.salary})"


class Manager:
    """A kind of Employee who also has a list of the people they manage.

    Exercise 2: created as Manager(name, salary, reports), with `reports`
    stored as an attribute. Let Employee's __init__ deal with name and
    salary by calling it through super(). Don't repeat its code.

    Exercise 3: describe() gives Employee's description followed by
    ", manages N people". Again, call the parent's version through
    super() and add to what it returns.

    >>> Manager("Grace", 90000, ["Ada", "Bob"]).describe()
    'Grace (£90000), manages 2 people'
    """


class Shape:
    """Given. The parent of every shape."""

    def area(self) -> float:
        raise NotImplementedError


class Square:
    """A kind of Shape, created with the length of its `side`."""


class Circle:
    """A kind of Shape, created with its `radius`. Use math.pi."""


def total_area(shapes: list[Shape]) -> float:
    """Return the combined area of all the shapes.

    This function must not check what kind of shape each one is. It asks
    each for its area and trusts it to answer. That is polymorphism.

    >>> total_area([Square(2), Square(3)])
    13
    """
    raise NotImplementedError


class PaymentMethod:
    """A way of paying. This is a template, not something you can create.

    Turn this into an abstract base class with one abstract method,
    pay(amount), using the two names imported at the top of this file.
    Then PaymentMethod() raises TypeError, and so does creating any
    subclass that forgot to write pay().
    """


class CardPayment:
    """A kind of PaymentMethod, created with the card's last four digits.

    >>> CardPayment("1234").pay(12.5)
    'Paid £12.50 with card ending 1234'
    """


class CashPayment:
    """A kind of PaymentMethod, for paying in cash.

    >>> CashPayment().pay(3)
    'Paid £3.00 in cash'
    """


class JsonMixin:
    """Adds a to_json() method to any class that inherits from it.

    to_json() returns the object's attributes as JSON text, with the keys
    in alphabetical order. vars(self) gives an object's attributes as a
    dict, and the json module does the rest.

    A mixin is a small class that isn't used alone. It exists to lend one
    ability to other classes.
    """


class Product:
    """A product with `name` and `price` attributes. It uses JsonMixin.

    >>> Product("pen", 2.5).to_json()
    '{"name": "pen", "price": 2.5}'
    """


class Notifier:
    """Given. The parent of everything that can send a message. (Stretch)

    send() returns a list of the messages that were sent.
    """

    def send(self, message: str) -> list[str]:
        raise NotImplementedError


class EmailNotifier:
    """A kind of Notifier, created with an address.

    Sends "Email to ADDRESS: MESSAGE".

    >>> EmailNotifier("ada@example.com").send("Hi")
    ['Email to ada@example.com: Hi']
    """


class SmsNotifier:
    """A kind of Notifier, created with a phone number.

    Sends "SMS to NUMBER: MESSAGE".

    Text messages are short, so only the first 20 characters of the
    message are sent.
    """


class MultiNotifier:
    """A kind of Notifier, created with a list of other notifiers.

    It sends each message through every one of them.

    send() returns all their messages in one list, in order. This class
    is a Notifier that contains other Notifiers (composition), so a
    MultiNotifier can itself be put inside another MultiNotifier.
    """
