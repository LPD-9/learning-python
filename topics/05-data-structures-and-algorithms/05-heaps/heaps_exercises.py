"""Heaps: always knowing the smallest item, without sorting everything.

Implement each one so the tests in test_heaps_exercises.py pass.
Run them with:  pytest topics/05-data-structures-and-algorithms/05-heaps

A heap keeps its smallest item ready at the front. Adding an item and
removing the smallest are both fast, even with millions of items. Use
one when you keep needing "the next smallest" while items are still
arriving, as in a priority queue.

Python's heapq module turns an ordinary list into a heap. Exercises 1 to
6 use it. In exercise 7 you build a heap yourself.
"""


def n_smallest(numbers: list[float], count: int) -> list[float]:
    """Return the count smallest numbers, smallest first.

    If count is more than the list holds, return them all. heapq has a
    function that does exactly this.

    >>> n_smallest([5, 1, 4, 2], 2)
    [1, 2]
    """
    raise NotImplementedError


def heap_sort(numbers: list[float]) -> list[float]:
    """Return a sorted copy of numbers, using a heap.

    Turn a copy of the list into a heap, then keep popping the smallest
    item until nothing is left. Don't use sorted() or .sort().

    >>> heap_sort([3, 1, 2])
    [1, 2, 3]
    """
    raise NotImplementedError


def kth_largest(numbers: list[float], k: int) -> float:
    """Return the k-th largest number, where k=1 means the largest.

    Duplicates count separately: the 2nd largest of [5, 5, 4] is 5.
    Raise ValueError if k is less than 1 or more than the list's length.

    >>> kth_largest([3, 1, 5, 2, 4], 2)
    4
    """
    raise NotImplementedError


def merge_sorted_lists(lists: list[list[float]]) -> list[float]:
    """Merge any number of sorted lists into one sorted list.

    You merged two sorted lists in the lists topic. A heap extends the
    idea to many: it always knows which list holds the smallest item
    not yet taken. heapq also has a function for this.

    >>> merge_sorted_lists([[1, 4], [2, 3], [0, 9]])
    [0, 1, 2, 3, 4, 9]
    """
    raise NotImplementedError


class TaskQueue:
    """A priority queue of tasks.

    add(task, priority) puts a task in the queue. pop() removes and
    returns the task with the lowest priority number, since 1 is more
    urgent than 5. Tasks with equal priority come out in the order they
    were added. pop() raises IndexError when the queue is empty.

    Store tuples in the heap. Tuples compare item by item, so think
    about what the second item needs to be to settle ties fairly, and
    to stop Python ever trying to compare two tasks with each other.

    >>> queue = TaskQueue()
    >>> queue.add("write report", priority=3)
    >>> queue.add("fix outage", priority=1)
    >>> queue.pop()
    'fix outage'
    """

    def __init__(self) -> None:
        raise NotImplementedError

    def add(self, task: object, priority: int) -> None:
        raise NotImplementedError

    def pop(self) -> object:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError


def min_merge_cost(sizes: list[int]) -> int:
    """Return the cheapest total cost of merging files into one.

    Merging two files costs the sum of their sizes and produces a file
    of that size. To keep the total low, always merge the two smallest
    files available, including files made by earlier merges.

    >>> min_merge_cost([4, 3, 2, 6])  # 2+3=5, then 4+5=9, then 6+9=15
    29
    """
    raise NotImplementedError


class MinHeap:
    """A heap written from scratch, without heapq. (Stretch)

    The heap is a list that represents a tree. The item at position i
    has its children at positions 2*i + 1 and 2*i + 2, and its parent at
    (i - 1) // 2. The one rule: a parent is never bigger than its
    children. That puts the smallest item at position 0.

    - push(item): add it at the end, then swap it upwards while it is
      smaller than its parent
    - pop(): take the item at position 0, move the last item into its
      place, then swap that downwards with its smaller child until the
      rule holds again. Raise IndexError if the heap is empty.
    - peek(): return the smallest item without removing it. Raise
      IndexError if the heap is empty.

    >>> heap = MinHeap()
    >>> for number in [5, 1, 3]:
    ...     heap.push(number)
    >>> heap.pop()
    1
    >>> heap.peek()
    3
    """

    def __init__(self) -> None:
        raise NotImplementedError

    def push(self, item: float) -> None:
        raise NotImplementedError

    def pop(self) -> float:
        raise NotImplementedError

    def peek(self) -> float:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError
