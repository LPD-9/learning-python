"""Encapsulation: controlling how an object's data is read and changed.

Implement each class so the tests in test_encapsulation_exercises.py pass.
Run them with:  pytest topics/04-oop/03-encapsulation

Python has no truly private attributes. It has conventions and one main
tool:

- a name starting with one underscore, such as `_balance`, means
  "internal: please don't touch this from outside"
- @property makes a method look like an attribute, so a class can
  compute, check or protect a value while callers still write
  `thing.value`

These stubs give you only a docstring. Every exercise needs @property.
"""


class Circle:
    """A circle with a `radius` attribute.

    `diameter` and `area` are worked out from the radius. Callers read
    them without brackets, and they are always up to date.

    >>> circle = Circle(2)
    >>> circle.diameter
    4
    >>> circle.radius = 5
    >>> circle.diameter
    10
    """


class Person:
    """A person with `first_name` and `last_name` attributes.

    `full_name` is read like an attribute and built from the other two.
    It can't be assigned to: trying must raise AttributeError, which is
    what a property does when it has no setter.

    >>> person = Person("Ada", "Lovelace")
    >>> person.full_name
    'Ada Lovelace'
    """


class Temperature:
    """A temperature stored as a `celsius` attribute.

    `fahrenheit` can be both read and assigned. Assigning to it updates
    celsius. (F = C * 9 / 5 + 32)

    >>> temperature = Temperature(100)
    >>> temperature.fahrenheit
    212.0
    >>> temperature.fahrenheit = 32
    >>> temperature.celsius
    0.0
    """


class Product:
    """A product with a `name` and a `price`.

    The price can never be negative. Assigning a negative price must
    raise ValueError and leave the old price in place. The same check
    must apply to the price passed in when the product is created.

    >>> product = Product("pen", 2.5)
    >>> product.price = 3
    >>> product.price
    3
    """


class User:
    """A user account, created with a username and an email.

    - `username` can be read but never changed (AttributeError).
    - `email` can be changed. Whatever is assigned is stored stripped of
      surrounding whitespace and in lowercase. An email without "@"
      raises ValueError.

    >>> user = User("ada", " Ada@Example.COM ")
    >>> user.email
    'ada@example.com'
    """


class Classroom:
    """A list of student names that can only be changed through methods.

    - add_student(name) adds a name, and raises ValueError if that name
      is already there.
    - `students` lets callers see the names, but changing what it returns
      must not change the classroom. Returning the internal list itself
      would hand callers the real thing: remember the mutability topic.

    >>> room = Classroom()
    >>> room.add_student("Ada")
    >>> len(room.students)
    1
    """


class BankAccount:
    """A bank account that protects its own state. (Stretch)

    Created as BankAccount(owner, pin, balance=0).

    - `balance` can be read but not assigned (AttributeError).
    - deposit(amount) and withdraw(amount) raise ValueError for amounts
      of zero or less, and for withdrawing more than the balance.
    - `history` gives the transactions so far as a tuple of
      (kind, amount) pairs, such as ("deposit", 50). Callers can't use it
      to change the account's records.
    - check_pin(pin) returns True or False. Store the PIN in an attribute
      whose name starts with two underscores, then look at what
      vars(account) shows. This is called name mangling.

    >>> account = BankAccount("Ada", pin="1234", balance=100)
    >>> account.deposit(50)
    >>> account.balance
    150
    >>> account.history
    (('deposit', 50),)
    """
