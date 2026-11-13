"""Hash maps: how dictionaries find things instantly, and what that buys you.

Implement each one so the tests in test_hash_maps_exercises.py pass.
Run them with:  pytest topics/05-data-structures-and-algorithms/04-hash-maps

A hash map (Python's dict) stores items in a row of numbered buckets. A
hash function turns each key into a number, and that number picks the
bucket. Looking a key up means hashing it and going straight to one
bucket, however many items are stored. Two keys landing in the same
bucket is called a collision, and every hash map needs a plan for it.

Exercises 2 to 5 use dicts to make slow code fast. In exercise 6 you
build a hash map yourself.
"""


def simple_hash(text: str, bucket_count: int) -> int:
    """Return the bucket number for text.

    Add up the character codes (see the built-in ord), then take the
    remainder after dividing by bucket_count. Real hash functions are
    cleverer, but they do the same job.

    >>> simple_hash("abc", 10)  # 97 + 98 + 99 = 294
    4
    """
    raise NotImplementedError


def two_sum_fast(numbers: list[int], target: int) -> tuple[int, int] | None:
    """Return the positions of two numbers that add up to target.

    You solved this with two nested loops in the loops topic. This time,
    go through the list once only. For each number, what other number
    would complete the pair, and how could a dict tell you instantly
    whether you've already seen it, and where?

    Return the positions smaller first, or None if no pair exists. The
    tests only use lists with one possible answer.

    >>> two_sum_fast([2, 7, 11, 15], 9)
    (0, 1)
    """
    raise NotImplementedError


def first_unique_char(text: str) -> str | None:
    """Return the first character that appears exactly once, or None.

    >>> first_unique_char("swiss")
    'w'
    """
    raise NotImplementedError


def are_anagrams(first: str, second: str) -> bool:
    """Return True if the two texts use exactly the same letters.

    Ignore case and spaces. Count the letters in a dict: don't sort.

    >>> are_anagrams("Listen", "Silent")
    True
    """
    raise NotImplementedError


def group_anagrams(words: list[str]) -> list[list[str]]:
    """Put words that are anagrams of each other into groups.

    Groups appear in the order their first word appears, and words keep
    their original order inside each group. The trick is to find a dict
    key that is identical for every word in a group.

    >>> group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    """
    raise NotImplementedError


class HashMap:
    """A hash map built from a list of buckets. Don't use a dict inside.

    Keep a list holding bucket_count buckets. Each bucket is a list of
    (key, value) pairs. The built-in hash(key) % bucket_count picks the
    bucket for a key. Keys that collide share a bucket, which you search
    with a loop. This plan for collisions is called chaining.

    >>> ages = HashMap()
    >>> ages.put("ada", 36)
    >>> ages.get("ada")
    36
    >>> "bob" in ages
    False
    """

    def __init__(self, bucket_count: int = 8) -> None:
        raise NotImplementedError

    def put(self, key: object, value: object) -> None:
        """Store value under key, replacing any value already there."""
        raise NotImplementedError

    def get(self, key: object, default: object = None) -> object:
        """Return the value stored under key, or default if there is none."""
        raise NotImplementedError

    def remove(self, key: object) -> None:
        """Delete key and its value. Raise KeyError if the key isn't there."""
        raise NotImplementedError

    def __contains__(self, key: object) -> bool:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError


class LRUCache:
    """A cache that holds a limited number of items. (Stretch)

    When it's full and a new key arrives, the least recently used key is
    thrown out. "Used" means read with get() or written with put().

    - get(key) returns the value, or None if the key isn't in the cache
    - put(key, value) adds or updates an item
    - len(cache) gives the number of items held

    Dicts remember the order keys were added. Think about how to move a
    key to the "most recent" end, or look up collections.OrderedDict.

    >>> cache = LRUCache(capacity=2)
    >>> cache.put("a", 1)
    >>> cache.put("b", 2)
    >>> cache.put("c", 3)
    >>> cache.get("a") is None
    True
    >>> cache.get("c")
    3
    """

    def __init__(self, capacity: int) -> None:
        raise NotImplementedError

    def get(self, key: object) -> object:
        raise NotImplementedError

    def put(self, key: object, value: object) -> None:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError
