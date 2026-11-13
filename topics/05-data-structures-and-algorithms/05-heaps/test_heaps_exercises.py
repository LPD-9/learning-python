import random

import pytest
from heaps_exercises import (
    MinHeap,
    TaskQueue,
    heap_sort,
    kth_largest,
    merge_sorted_lists,
    min_merge_cost,
    n_smallest,
)


class TestNSmallest:
    def test_example(self):
        assert n_smallest([5, 1, 4, 2], 2) == [1, 2]

    def test_count_bigger_than_the_list(self):
        assert n_smallest([3, 1], 10) == [1, 3]

    def test_zero(self):
        assert n_smallest([3, 1], 0) == []

    def test_original_is_unchanged(self):
        numbers = [3, 1, 2]
        n_smallest(numbers, 2)
        assert numbers == [3, 1, 2]


class TestHeapSort:
    def test_example(self):
        assert heap_sort([3, 1, 2]) == [1, 2, 3]

    def test_duplicates(self):
        assert heap_sort([2, 3, 2, 1, 3]) == [1, 2, 2, 3, 3]

    def test_empty(self):
        assert heap_sort([]) == []

    def test_original_is_unchanged(self):
        numbers = [3, 1, 2]
        heap_sort(numbers)
        assert numbers == [3, 1, 2]


class TestKthLargest:
    def test_example(self):
        assert kth_largest([3, 1, 5, 2, 4], 2) == 4

    def test_largest_and_smallest(self):
        assert kth_largest([3, 1, 5], 1) == 5
        assert kth_largest([3, 1, 5], 3) == 1

    def test_duplicates_count_separately(self):
        assert kth_largest([5, 5, 4], 2) == 5

    @pytest.mark.parametrize("k", [0, -1, 4])
    def test_k_out_of_range(self, k):
        with pytest.raises(ValueError):
            kth_largest([3, 1, 5], k)


class TestMergeSortedLists:
    def test_example(self):
        assert merge_sorted_lists([[1, 4], [2, 3], [0, 9]]) == [0, 1, 2, 3, 4, 9]

    def test_empty_lists_among_them(self):
        assert merge_sorted_lists([[], [1, 2], []]) == [1, 2]

    def test_single_list(self):
        assert merge_sorted_lists([[1, 2, 3]]) == [1, 2, 3]

    def test_no_lists(self):
        assert merge_sorted_lists([]) == []

    def test_returns_a_list(self):
        assert isinstance(merge_sorted_lists([[1], [2]]), list)


class TestTaskQueue:
    def test_lowest_number_comes_out_first(self):
        queue = TaskQueue()
        queue.add("write report", priority=3)
        queue.add("fix outage", priority=1)
        queue.add("reply to email", priority=2)
        order = [queue.pop(), queue.pop(), queue.pop()]
        assert order == ["fix outage", "reply to email", "write report"]

    def test_equal_priority_keeps_arrival_order(self):
        queue = TaskQueue()
        for task in ["zebra", "apple", "mango"]:
            queue.add(task, priority=1)
        assert [queue.pop(), queue.pop(), queue.pop()] == ["zebra", "apple", "mango"]

    def test_tasks_that_cannot_be_compared(self):
        queue = TaskQueue()
        queue.add({"name": "first"}, priority=1)
        queue.add({"name": "second"}, priority=1)
        assert queue.pop() == {"name": "first"}

    def test_len(self):
        queue = TaskQueue()
        assert len(queue) == 0
        queue.add("a", priority=1)
        queue.add("b", priority=1)
        queue.pop()
        assert len(queue) == 1

    def test_pop_when_empty(self):
        with pytest.raises(IndexError):
            TaskQueue().pop()


class TestMinMergeCost:
    def test_example(self):
        assert min_merge_cost([4, 3, 2, 6]) == 29

    def test_two_files(self):
        assert min_merge_cost([1, 2]) == 3

    def test_one_file_needs_no_merging(self):
        assert min_merge_cost([5]) == 0

    def test_no_files(self):
        assert min_merge_cost([]) == 0

    def test_equal_sizes(self):
        assert min_merge_cost([1, 1, 1, 1]) == 8

    def test_original_is_unchanged(self):
        sizes = [4, 3, 2, 6]
        min_merge_cost(sizes)
        assert sizes == [4, 3, 2, 6]


class TestMinHeap:
    def test_example(self):
        heap = MinHeap()
        for number in [5, 1, 3]:
            heap.push(number)
        assert heap.pop() == 1
        assert heap.peek() == 3

    def test_pops_come_out_in_order(self):
        heap = MinHeap()
        for number in [7, 2, 9, 4, 1, 8, 3]:
            heap.push(number)
        assert [heap.pop() for _ in range(7)] == [1, 2, 3, 4, 7, 8, 9]

    def test_duplicates(self):
        heap = MinHeap()
        for number in [2, 1, 2, 1]:
            heap.push(number)
        assert [heap.pop() for _ in range(4)] == [1, 1, 2, 2]

    def test_len(self):
        heap = MinHeap()
        assert len(heap) == 0
        heap.push(1)
        heap.push(2)
        heap.pop()
        assert len(heap) == 1

    def test_peek_does_not_remove(self):
        heap = MinHeap()
        heap.push(4)
        assert heap.peek() == 4
        assert len(heap) == 1

    def test_empty(self):
        with pytest.raises(IndexError):
            MinHeap().pop()
        with pytest.raises(IndexError):
            MinHeap().peek()

    def test_mixing_pushes_and_pops(self):
        heap = MinHeap()
        heap.push(5)
        heap.push(3)
        assert heap.pop() == 3
        heap.push(1)
        heap.push(4)
        assert [heap.pop(), heap.pop(), heap.pop()] == [1, 4, 5]

    def test_many_random_numbers(self):
        numbers = random.Random(7).sample(range(10_000), 500)
        heap = MinHeap()
        for number in numbers:
            heap.push(number)
        assert [heap.pop() for _ in numbers] == sorted(numbers)
