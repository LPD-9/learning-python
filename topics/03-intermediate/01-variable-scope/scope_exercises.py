"""Variable scope: local and global names, closures and nonlocal.

Implement each function so the tests in test_scope_exercises.py pass.
Run them with:  pytest topics/03-intermediate/01-variable-scope

Python looks a name up in four places, in this order: Local, Enclosing
function, Global (the module), Built-in. This is called the LEGB rule.

Before you start, predict what the last line shows, then run it:
    >>> x = 10
    >>> def change():
    ...     x = 20
    >>> change()
    >>> x
"""

from collections.abc import Callable

DISCOUNT_RATE = 0.1
PLUGINS: list[str] = []
_last_ticket = 0


def apply_discount(price: float) -> float:
    """Return price reduced by DISCOUNT_RATE, the constant defined above.

    Read the constant by name. Don't copy its value into the function:
    the tests change the constant and expect the function to follow.

    >>> apply_discount(200)
    180.0
    """
    raise NotImplementedError


def register_plugin(name: str) -> int:
    """Add name to the PLUGINS list above and return how many there are now.

    You can change a module-level list from inside a function without any
    special keyword. After the next exercise, work out why this one is
    different.
    """
    raise NotImplementedError


def next_ticket_number() -> int:
    """Add 1 to _last_ticket, defined above, and return the new value.

    Assigning to a module-level name from inside a function needs a
    keyword. Without it Python raises UnboundLocalError. Try it without
    first and read the error message.
    """
    raise NotImplementedError


def make_greeter(greeting: str) -> Callable[[str], str]:
    """Return a function that greets people with the given greeting.

    >>> hello = make_greeter("Hello")
    >>> hello("Ada")
    'Hello, Ada!'
    """
    raise NotImplementedError


def make_accumulator(start: float) -> Callable[[float], float]:
    """Return a function that keeps a running total, beginning at start.

    Each call adds its argument to the total and returns the new total.

    >>> add = make_accumulator(10)
    >>> add(5)
    15
    >>> add(2)
    17
    """
    raise NotImplementedError


def make_multipliers(count: int) -> list[Callable[[int], int]]:
    """Return a list of functions, where function number i multiplies by i.

    >>> double = make_multipliers(3)[2]
    >>> double(10)
    20

    There is a well-known trap here. If every function you get back
    multiplies by the same number, look up "late binding closures".
    """
    raise NotImplementedError


def make_account(
    balance: float,
) -> tuple[Callable[[float], float], Callable[[], float]]:
    """Return two functions that share one balance. (Stretch)

    The first, deposit(amount), adds to the balance and returns the new
    balance. The second, get_balance(), returns the current balance.
    Accounts made by separate calls must not affect each other.

    >>> deposit, get_balance = make_account(100)
    >>> deposit(50)
    150
    >>> get_balance()
    150
    """
    raise NotImplementedError
