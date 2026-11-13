"""Dictionaries: lookups, .get(), counting, grouping and nesting.

Implement each function so the tests in test_dictionaries_exercises.py pass.
Run them with:  pytest topics/02-fundamentals/04-dictionaries
"""


def count_words(text: str) -> dict[str, int]:
    """Count how many times each word appears in text.

    Words are separated by whitespace. Treat words case-insensitively
    (store them lowercase) and strip the punctuation characters . , ! ?
    from the start and end of each word.

    >>> count_words("The cat. The hat!")
    {'the': 2, 'cat': 1, 'hat': 1}
    """
    raise NotImplementedError


def rename_keys(record: dict, renames: dict[str, str]) -> dict:
    """Return a copy of record with keys renamed according to renames.

    Keys not mentioned in renames keep their name. Don't modify record.

    >>> rename_keys({"fname": "Ada", "age": 36}, {"fname": "first_name"})
    {'first_name': 'Ada', 'age': 36}
    """
    raise NotImplementedError


def invert_roles(user_roles: dict[str, str]) -> dict[str, list[str]]:
    """Turn a {user: role} mapping into {role: [users]}.

    Each list of users must be sorted alphabetically.

    >>> invert_roles({"bob": "user", "alice": "admin", "carol": "admin"})
    {'user': ['bob'], 'admin': ['alice', 'carol']}
    """
    raise NotImplementedError


def top_n(counts: dict[str, int], n: int) -> list[str]:
    """Return the n keys with the highest counts, highest first.

    Break ties alphabetically. If n is bigger than the dict, return all keys.

    >>> top_n({"a": 1, "b": 5, "c": 3, "d": 5}, 3)
    ['b', 'd', 'c']
    """
    raise NotImplementedError


def merge_inventories(first: dict[str, int], second: dict[str, int]) -> dict[str, int]:
    """Combine two stock counts into one. (Stretch)

    Quantities for the same item are added together. Leave out any item
    whose combined quantity is zero or less (negative numbers mean stock
    was removed). Do NOT modify either input dictionary.

    >>> merge_inventories({"apple": 3, "pear": 1}, {"apple": 2, "pear": -1})
    {'apple': 5}
    """
    raise NotImplementedError


def get_nested(data: dict, path: str, default: object = None) -> object:
    """Look up a value in nested dicts using a dotted path. (Stretch)

    Return default if any part of the path is missing.

    >>> config = {"db": {"host": "localhost", "port": 5432}}
    >>> get_nested(config, "db.port")
    5432
    >>> get_nested(config, "db.user", "admin")
    'admin'
    """
    raise NotImplementedError
