"""Stacks and queues: collections with a rule about what comes out next.

Implement each one so the tests in test_stacks_and_queues_exercises.py pass.
Run them with:
    pytest topics/05-data-structures-and-algorithms/03-stacks-and-queues

A stack is last in, first out, like a pile of plates: you add to the top
and take from the top. A queue is first in, first out, like a line of
people: you join at the back and leave from the front.

A Python list makes a good stack, because append and pop both work at
the end. It makes a slow queue, because removing from the front shifts
every other item. collections.deque is fast at both ends.
"""


class Stack:
    """A last in, first out collection.

    >>> plates = Stack()
    >>> plates.push("blue")
    >>> plates.push("red")
    >>> plates.pop()
    'red'
    >>> plates.peek()
    'blue'
    """

    def __init__(self) -> None:
        raise NotImplementedError

    def push(self, item: object) -> None:
        raise NotImplementedError

    def pop(self) -> object:
        """Remove and return the top item. Raise IndexError if empty."""
        raise NotImplementedError

    def peek(self) -> object:
        """Return the top item without removing it. Raise IndexError if empty."""
        raise NotImplementedError

    def is_empty(self) -> bool:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError


class Queue:
    """A first in, first out collection. Build it on collections.deque.

    >>> line = Queue()
    >>> line.enqueue("ada")
    >>> line.enqueue("bob")
    >>> line.dequeue()
    'ada'
    """

    def __init__(self) -> None:
        raise NotImplementedError

    def enqueue(self, item: object) -> None:
        raise NotImplementedError

    def dequeue(self) -> object:
        """Remove and return the item at the front. Raise IndexError if empty."""
        raise NotImplementedError

    def is_empty(self) -> bool:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError


def is_balanced(text: str) -> bool:
    """Return True if every bracket in text is closed in the right order.

    The brackets are (), [] and {}. Other characters are ignored. This
    is how editors spot a missing bracket. Push each opening bracket on
    a stack. What should be on top when you meet a closing bracket?

    >>> is_balanced("print(items[0])")
    True
    >>> is_balanced("(]")
    False
    """
    raise NotImplementedError


class TextEditor:
    """A text editor with undo.

    type(text) adds text to the end. undo() takes back the most recent
    type() that hasn't been undone, and does nothing if there is none.
    The current contents are in the `text` attribute.

    >>> editor = TextEditor()
    >>> editor.type("Hello")
    >>> editor.type(" world")
    >>> editor.undo()
    >>> editor.text
    'Hello'
    """

    def __init__(self) -> None:
        raise NotImplementedError

    def type(self, text: str) -> None:
        raise NotImplementedError

    def undo(self) -> None:
        raise NotImplementedError


def round_robin(tasks: dict[str, int], time_slice: int) -> list[str]:
    """Return the order in which tasks finish when they take turns.

    tasks maps each task's name to the units of work it needs. Tasks
    wait in a queue in the order given. The task at the front does up to
    time_slice units of work. If that finishes it, it's done. If not, it
    goes to the back of the queue. This is how an operating system shares
    one processor between many programs.

    >>> round_robin({"a": 3, "b": 1, "c": 2}, time_slice=1)
    ['b', 'c', 'a']
    """
    raise NotImplementedError


def evaluate_rpn(tokens: list[str]) -> float:
    """Work out a sum written in reverse Polish notation.

    The operator comes after its two numbers, so "2 3 +" means 2 + 3, and
    no brackets are ever needed: "2 3 + 4 *" means (2 + 3) * 4.

    Read the tokens left to right. Push each number on a stack. For an
    operator (+, -, *, /), pop two numbers, apply it, and push the
    result. Mind which number was pushed first: "10 2 -" is 8.

    Raise ValueError if the expression is malformed: an operator without
    two numbers to work on, or anything other than exactly one number
    left at the end.

    >>> evaluate_rpn(["2", "3", "+", "4", "*"])
    20.0
    """
    raise NotImplementedError


class MinStack:
    """A stack that can also report its smallest item instantly. (Stretch)

    push, pop and peek work as on Stack. minimum() returns the smallest
    item currently on the stack, without searching through it. pop and
    minimum raise IndexError when the stack is empty.

    The difficulty is pop: when the smallest item leaves, how do you know
    the next smallest without looking? Consider keeping a second stack.

    >>> stack = MinStack()
    >>> stack.push(5)
    >>> stack.push(2)
    >>> stack.minimum()
    2
    >>> stack.pop()
    2
    >>> stack.minimum()
    5
    """

    def __init__(self) -> None:
        raise NotImplementedError

    def push(self, item: float) -> None:
        raise NotImplementedError

    def pop(self) -> float:
        raise NotImplementedError

    def peek(self) -> float:
        raise NotImplementedError

    def minimum(self) -> float:
        raise NotImplementedError
