"""The bugs that test_my_tests_catch_bugs.py plants in testing_exercises.py.

SPOILERS: reading this list tells you what to test. Try without it first.






















Each entry is (function, hint, original code, broken code).
"""

BUGS = [
    ("add_vat", "the VAT rate", "price * 1.2, 2", "price * 1.25, 2"),
    (
        "add_vat",
        "a price where rounding matters",
        "round(price * 1.2, 2)",
        "price * 1.2",
    ),
    ("is_adult", "the exact age where adulthood starts", "age >= 18", "age > 18"),
    ("withdraw", "an amount of exactly zero", "if amount <= 0:", "if amount < 0:"),
    (
        "withdraw",
        "taking out more than the balance",
        "if amount > balance:",
        "if False:",
    ),
    ("slugify", "capital letters", "title.lower()", "title"),
    (
        "slugify",
        "punctuation at the start or end",
        'return slug.strip("-")',
        "return slug",
    ),
    (
        "slugify",
        "several spaces or symbols in a row",
        'r"[^a-z0-9]+"',
        'r"[^a-z0-9]"',
    ),
    (
        "Basket.item_count",
        "an item added with a quantity above 1",
        "sum(quantity for _, _, quantity in self._lines)",
        "len(self._lines)",
    ),
    (
        "Basket.total",
        "an item added with a quantity above 1",
        "price * quantity for",
        "price for",
    ),
    (
        "save_high_score",
        "saving twice to the same file, then reading the file",
        'path.open("a"',
        'path.open("w"',
    ),
    (
        "save_high_score",
        "saving a lower score after a higher one",
        'return max(int(line.split(",")[1]) for line in lines)',
        "return score",
    ),
    ("greeting", "exactly 12 o'clock", "if hour < 12:", "if hour <= 12:"),
    ("greeting", "the last hour of the afternoon", "if hour < 18:", "if hour < 17:"),
]
