import pytest
from stacks_and_queues_exercises import (
    MinStack,
    Queue,
    Stack,
    TextEditor,
    evaluate_rpn,
    is_balanced,
    round_robin,
)


class TestStack:
    def test_starts_empty(self):
        stack = Stack()
        assert stack.is_empty() is True
        assert len(stack) == 0

    def test_last_in_first_out(self):
        stack = Stack()
        for item in ["a", "b", "c"]:
            stack.push(item)
        assert [stack.pop(), stack.pop(), stack.pop()] == ["c", "b", "a"]

    def test_peek_does_not_remove(self):
        stack = Stack()
        stack.push("a")
        assert stack.peek() == "a"
        assert len(stack) == 1

    def test_len_and_is_empty(self):
        stack = Stack()
        stack.push("a")
        assert stack.is_empty() is False
        stack.pop()
        assert stack.is_empty() is True

    def test_pop_and_peek_when_empty(self):
        with pytest.raises(IndexError):
            Stack().pop()
        with pytest.raises(IndexError):
            Stack().peek()

    def test_stacks_are_independent(self):
        first, second = Stack(), Stack()
        first.push(1)
        assert second.is_empty() is True


class TestQueue:
    def test_starts_empty(self):
        queue = Queue()
        assert queue.is_empty() is True
        assert len(queue) == 0

    def test_first_in_first_out(self):
        queue = Queue()
        for item in ["a", "b", "c"]:
            queue.enqueue(item)
        assert [queue.dequeue(), queue.dequeue(), queue.dequeue()] == ["a", "b", "c"]

    def test_len(self):
        queue = Queue()
        queue.enqueue("a")
        queue.enqueue("b")
        queue.dequeue()
        assert len(queue) == 1

    def test_dequeue_when_empty(self):
        with pytest.raises(IndexError):
            Queue().dequeue()


class TestIsBalanced:
    @pytest.mark.parametrize(
        "text",
        ["", "()", "([]{})", "print(items[0])", "{'a': [1, (2, 3)]}", "no brackets"],
    )
    def test_balanced(self, text):
        assert is_balanced(text) is True

    @pytest.mark.parametrize("text", ["(", ")", "(]", "([)]", "(()", "())", "]["])
    def test_not_balanced(self, text):
        assert is_balanced(text) is False


class TestTextEditor:
    def test_starts_blank(self):
        assert TextEditor().text == ""

    def test_typing(self):
        editor = TextEditor()
        editor.type("Hello")
        editor.type(" world")
        assert editor.text == "Hello world"

    def test_undo(self):
        editor = TextEditor()
        editor.type("Hello")
        editor.type(" world")
        editor.undo()
        assert editor.text == "Hello"

    def test_undo_several_times(self):
        editor = TextEditor()
        editor.type("a")
        editor.type("b")
        editor.type("c")
        editor.undo()
        editor.undo()
        assert editor.text == "a"

    def test_undo_with_nothing_to_undo(self):
        editor = TextEditor()
        editor.undo()
        assert editor.text == ""

    def test_typing_after_undo(self):
        editor = TextEditor()
        editor.type("a")
        editor.type("b")
        editor.undo()
        editor.type("c")
        assert editor.text == "ac"
        editor.undo()
        editor.undo()
        assert editor.text == ""


class TestRoundRobin:
    def test_example(self):
        assert round_robin({"a": 3, "b": 1, "c": 2}, time_slice=1) == ["b", "c", "a"]

    def test_bigger_slice(self):
        assert round_robin({"a": 3, "b": 1, "c": 2}, time_slice=2) == ["b", "c", "a"]

    def test_slice_big_enough_for_everything(self):
        assert round_robin({"long": 5, "short": 1}, time_slice=5) == ["long", "short"]

    def test_equal_tasks_finish_in_order(self):
        assert round_robin({"x": 2, "y": 2}, time_slice=1) == ["x", "y"]

    def test_no_tasks(self):
        assert round_robin({}, time_slice=3) == []

    def test_input_is_not_changed(self):
        tasks = {"a": 3, "b": 1}
        round_robin(tasks, time_slice=1)
        assert tasks == {"a": 3, "b": 1}


class TestEvaluateRpn:
    def test_addition(self):
        assert evaluate_rpn(["2", "3", "+"]) == 5

    def test_example(self):
        assert evaluate_rpn(["2", "3", "+", "4", "*"]) == 20

    def test_order_matters_for_subtraction(self):
        assert evaluate_rpn(["10", "2", "-"]) == 8

    def test_order_matters_for_division(self):
        assert evaluate_rpn(["8", "2", "/"]) == 4

    def test_single_number(self):
        assert evaluate_rpn(["5"]) == 5

    def test_decimals_and_negatives(self):
        assert evaluate_rpn(["1.5", "-2", "*"]) == -3

    def test_longer_expression(self):
        # (5 + ((1 + 2) * 4)) - 3
        assert evaluate_rpn(["5", "1", "2", "+", "4", "*", "+", "3", "-"]) == 14

    @pytest.mark.parametrize("tokens", [["+"], ["1", "+"], ["1", "2"], []])
    def test_malformed(self, tokens):
        with pytest.raises(ValueError):
            evaluate_rpn(tokens)


class TestMinStack:
    def test_example(self):
        stack = MinStack()
        stack.push(5)
        stack.push(2)
        assert stack.minimum() == 2
        assert stack.pop() == 2
        assert stack.minimum() == 5

    def test_behaves_like_a_stack(self):
        stack = MinStack()
        stack.push(1)
        stack.push(2)
        assert stack.peek() == 2
        assert stack.pop() == 2
        assert stack.pop() == 1

    def test_minimum_below_the_top(self):
        stack = MinStack()
        for item in [3, 1, 4]:
            stack.push(item)
        assert stack.minimum() == 1
        stack.pop()
        assert stack.minimum() == 1
        stack.pop()
        assert stack.minimum() == 3

    def test_duplicate_minimums(self):
        stack = MinStack()
        for item in [2, 2, 5]:
            stack.push(item)
        stack.pop()
        stack.pop()
        assert stack.minimum() == 2

    def test_empty(self):
        with pytest.raises(IndexError):
            MinStack().pop()
        with pytest.raises(IndexError):
            MinStack().minimum()
