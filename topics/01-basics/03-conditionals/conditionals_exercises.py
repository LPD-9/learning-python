"""Conditionals: if/elif/else, guard clauses and match.

Implement each function so the tests in test_conditionals_exercises.py pass.
Run them with:  pytest topics/01-basics/03-conditionals
"""


def sign(n: float) -> str:
    """Return "positive", "negative" or "zero".

    >>> sign(-3)
    'negative'
    """
    raise NotImplementedError


def ticket_price(age: int) -> int:
    """Return the cinema ticket price in pounds for someone's age.

    Children under 13 pay 5. People aged 65 or over pay 7.
    Everyone else pays 10.

    >>> ticket_price(30)
    10
    """
    raise NotImplementedError


def grade(score: int) -> str:
    """Turn a test score from 0 to 100 into a letter grade.

    90 or more is "A", 80 or more is "B", 70 or more is "C",
    60 or more is "D", and anything lower is "F".

    >>> grade(85)
    'B'
    """
    raise NotImplementedError


def fizzbuzz_value(n: int) -> str:
    """Return the FizzBuzz answer for one number.

    Multiples of 3 give "Fizz", multiples of 5 give "Buzz", multiples of
    both give "FizzBuzz". Any other number is returned as a string.
    Think about which check has to come first.

    >>> fizzbuzz_value(9)
    'Fizz'
    >>> fizzbuzz_value(7)
    '7'
    """
    raise NotImplementedError


def shipping_cost(weight_kg: float, express: bool) -> float:
    """Return the cost in pounds of posting a parcel.

    Up to and including 1 kg costs 3.00. Up to and including 5 kg costs
    6.00. Anything heavier costs 10.00. Express delivery doubles the cost.

    >>> shipping_cost(2, express=False)
    6.0
    >>> shipping_cost(2, express=True)
    12.0
    """
    raise NotImplementedError


def http_status_text(code: int) -> str:
    """Describe an HTTP status code.

    200 is "OK", 404 is "Not Found" and 500 is "Server Error".
    Any other code from 400 to 499 is "Client Error", any other code
    from 500 to 599 is "Server Error", and everything else is "Unknown".

    This is a good place to try the match statement.

    >>> http_status_text(404)
    'Not Found'
    >>> http_status_text(403)
    'Client Error'
    """
    raise NotImplementedError


def triangle_type(a: float, b: float, c: float) -> str:
    """Classify a triangle by the lengths of its sides. (Stretch)

    Return "invalid" if any side is zero or less, or if the two shorter
    sides together are not longer than the longest side (the sides
    couldn't meet). Otherwise return "equilateral" (all sides equal),
    "isosceles" (exactly two equal) or "scalene" (none equal).

    Deal with the invalid cases first, as guard clauses.

    >>> triangle_type(3, 3, 3)
    'equilateral'
    >>> triangle_type(1, 2, 10)
    'invalid'
    """
    raise NotImplementedError
