"""Variables and syntax: assignment, expressions, return values and f-strings.

Implement each function so the tests in test_variables_exercises.py pass.
Run them with:  pytest topics/01-basics/01-variables-and-syntax
"""


def rectangle_area(width: float, height: float) -> float:
    """Return the area of a rectangle.

    >>> rectangle_area(3, 4)
    12
    """
    raise NotImplementedError


def full_name(first: str, last: str) -> str:
    """Join a first and last name with a single space between them.

    >>> full_name("Ada", "Lovelace")
    'Ada Lovelace'
    """
    raise NotImplementedError


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a temperature from Celsius to Fahrenheit.

    Multiply by 9, divide by 5, then add 32.

    >>> celsius_to_fahrenheit(100)
    212.0
    """
    raise NotImplementedError


def swap(a: object, b: object) -> tuple[object, object]:
    """Return the two values in the opposite order.

    Python can return more than one value at once. Find out how.

    >>> swap(1, 2)
    (2, 1)
    """
    raise NotImplementedError


def type_name(value: object) -> str:
    """Return the name of value's type, as a string.

    Every value in Python has a type. The built-in type() tells you what
    it is, and every type has a __name__.

    >>> type_name(42)
    'int'
    >>> type_name("hello")
    'str'
    """
    raise NotImplementedError


def receipt_line(item: str, quantity: int, unit_price: float) -> str:
    """Format one line of a shop receipt.

    Prices are shown with a pound sign and exactly two decimal places.
    Work out the line total in a variable first, then build the string.

    >>> receipt_line("Coffee", 3, 2.5)
    '3 x Coffee @ £2.50 = £7.50'
    """
    raise NotImplementedError


def compound_interest(principal: float, rate_percent: float, years: int) -> float:
    """Return what savings are worth after earning yearly interest. (Stretch)

    Each year the balance grows by rate_percent. So after one year at 5%,
    1000 becomes 1050, and after two years it becomes 1102.50, because the
    second year's interest is paid on 1050, not on 1000.

    Round the result to 2 decimal places. Break the calculation into
    named steps instead of writing it all on one line.

    >>> compound_interest(1000, 5, 2)
    1102.5
    """
    raise NotImplementedError
