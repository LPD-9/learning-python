import pytest
from linked_lists_exercises import (
    LinkedList,
    Node,
    append,
    length,
    push_front,
    remove,
    reverse,
    to_list,
)


def chain(*values):
    """Build a chain of nodes by hand and return its head."""
    head = None
    for value in reversed(values):
        head = Node(value, head)
    return head


def values(head):
    """Read a chain by hand, giving up if it seems to loop for ever."""
    result = []
    while head is not None:
        result.append(head.value)
        head = head.next
        assert len(result) < 1000, "the chain loops back on itself"
    return result


class TestToList:
    def test_example(self):
        assert to_list(chain(1, 2, 3)) == [1, 2, 3]

    def test_single(self):
        assert to_list(chain("only")) == ["only"]

    def test_empty(self):
        assert to_list(None) == []


class TestLength:
    def test_example(self):
        assert length(chain("a", "b")) == 2

    def test_single(self):
        assert length(chain("a")) == 1

    def test_empty(self):
        assert length(None) == 0


class TestPushFront:
    def test_example(self):
        assert values(push_front(chain(2, 3), 1)) == [1, 2, 3]

    def test_onto_an_empty_chain(self):
        assert values(push_front(None, 1)) == [1]

    def test_existing_nodes_are_reused(self):
        old_head = chain(2, 3)
        assert push_front(old_head, 1).next is old_head


class TestAppend:
    def test_example(self):
        assert values(append(chain(1, 2), 3)) == [1, 2, 3]

    def test_head_stays_the_same(self):
        head = chain(1, 2)
        assert append(head, 3) is head

    def test_onto_an_empty_chain(self):
        assert values(append(None, 1)) == [1]


class TestRemove:
    def test_from_the_middle(self):
        assert values(remove(chain(1, 2, 3), 2)) == [1, 3]

    def test_the_head(self):
        assert values(remove(chain(1, 2, 3), 1)) == [2, 3]

    def test_the_last_node(self):
        assert values(remove(chain(1, 2, 3), 3)) == [1, 2]

    def test_only_the_first_match(self):
        assert values(remove(chain(1, 2, 1), 1)) == [2, 1]

    def test_value_not_present(self):
        assert values(remove(chain(1, 2), 9)) == [1, 2]

    def test_the_only_node(self):
        assert remove(chain(1), 1) is None

    def test_empty(self):
        assert remove(None, 1) is None


class TestReverse:
    def test_example(self):
        assert values(reverse(chain(1, 2, 3))) == [3, 2, 1]

    def test_two_nodes(self):
        assert values(reverse(chain(1, 2))) == [2, 1]

    def test_single(self):
        assert values(reverse(chain(1))) == [1]

    def test_empty(self):
        assert reverse(None) is None

    def test_no_new_nodes_are_made(self):
        head = chain(1, 2, 3)
        last = head.next.next
        assert reverse(head) is last
        assert head.next is None


class TestLinkedList:
    def test_starts_empty(self):
        items = LinkedList()
        assert len(items) == 0
        assert list(items) == []

    def test_append(self):
        items = LinkedList()
        items.append(1)
        items.append(2)
        assert list(items) == [1, 2]
        assert len(items) == 2

    def test_prepend(self):
        items = LinkedList()
        items.prepend(2)
        items.prepend(1)
        assert list(items) == [1, 2]

    def test_mixing_append_and_prepend(self):
        items = LinkedList()
        items.append("b")
        items.prepend("a")
        items.append("c")
        assert list(items) == ["a", "b", "c"]

    def test_pop_front(self):
        items = LinkedList()
        items.append(1)
        items.append(2)
        assert items.pop_front() == 1
        assert list(items) == [2]
        assert len(items) == 1

    def test_pop_front_when_empty(self):
        with pytest.raises(IndexError):
            LinkedList().pop_front()

    def test_append_after_emptying(self):
        items = LinkedList()
        items.append(1)
        items.pop_front()
        items.append(2)
        items.append(3)
        assert list(items) == [2, 3]

    def test_can_be_looped_over_twice(self):
        items = LinkedList()
        items.append(1)
        assert list(items) == [1]
        assert list(items) == [1]
