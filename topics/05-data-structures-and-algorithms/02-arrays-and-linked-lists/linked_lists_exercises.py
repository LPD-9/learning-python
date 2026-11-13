"""Arrays and linked lists: two ways of keeping items in order.

Implement each one so the tests in test_linked_lists_exercises.py pass.
Run them with:
    pytest topics/05-data-structures-and-algorithms/02-arrays-and-linked-lists

A Python list is an array: its items sit side by side in memory. That
makes items[500] instant, but inserting at the front means shuffling
every other item along by one.

A linked list is a chain of nodes. Each node holds a value and a
reference to the next node, and the last node's `next` is None. Adding
at the front is instant, but reaching item 500 means following 500
links. Neither is better. They are good at different things.

In these exercises a list is represented by its first node, called the
head. An empty list is None. Don't convert to a Python list to do the
work, except in to_list, where that is the job.
"""

from collections.abc import Iterator


class Node:
    """Given. One link in the chain."""

    def __init__(self, value: object, next: Node | None = None) -> None:
        self.value = value
        self.next = next


def to_list(head: Node | None) -> list:
    """Return the values in the chain as a Python list, first to last.

    Start at the head and keep following `next` until you reach None.

    >>> to_list(Node(1, Node(2, Node(3))))
    [1, 2, 3]
    """
    raise NotImplementedError


def length(head: Node | None) -> int:
    """Return the number of nodes in the chain.

    >>> length(Node("a", Node("b")))
    2
    """
    raise NotImplementedError


def push_front(head: Node | None, value: object) -> Node:
    """Add a value at the front and return the new head.

    This takes the same time however long the chain is.

    >>> to_list(push_front(Node(2, Node(3)), 1))
    [1, 2, 3]
    """
    raise NotImplementedError


def append(head: Node | None, value: object) -> Node:
    """Add a value at the end and return the head.

    The head only changes when the chain was empty.

    >>> to_list(append(Node(1, Node(2)), 3))
    [1, 2, 3]
    """
    raise NotImplementedError


def remove(head: Node | None, value: object) -> Node | None:
    """Remove the first node holding value, and return the head.

    To remove a node, make the node before it point to the node after
    it. Removing the head itself is a special case. If the value isn't
    there, nothing changes.

    >>> to_list(remove(Node(1, Node(2, Node(3))), 2))
    [1, 3]
    """
    raise NotImplementedError


def reverse(head: Node | None) -> Node | None:
    """Reverse the chain by re-pointing its links, and return the new head.

    Don't create any new nodes. Walk along the chain, turning each
    node's `next` to point backwards. Draw three nodes on paper first:
    you need to remember the previous node, and to save the next one
    before you overwrite the link to it.

    >>> to_list(reverse(Node(1, Node(2, Node(3)))))
    [3, 2, 1]
    """
    raise NotImplementedError


class LinkedList:
    """A linked list wrapped in a class, so callers never see nodes. (Stretch)

    - append(value) adds at the end
    - prepend(value) adds at the front
    - pop_front() removes and returns the first value, and raises
      IndexError when the list is empty
    - len(the_list) gives the number of values
    - a for loop over the list gives the values in order

    append must not walk the whole chain. Keep a reference to the last
    node as well as the first, and keep a count instead of counting.

    >>> queue = LinkedList()
    >>> queue.append("b")
    >>> queue.prepend("a")
    >>> list(queue)
    ['a', 'b']
    """

    def __init__(self) -> None:
        raise NotImplementedError

    def append(self, value: object) -> None:
        raise NotImplementedError

    def prepend(self, value: object) -> None:
        raise NotImplementedError

    def pop_front(self) -> object:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError

    def __iter__(self) -> Iterator:
        raise NotImplementedError
