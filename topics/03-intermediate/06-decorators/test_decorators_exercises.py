import decorators_exercises
import pytest
from decorators_exercises import (
    announce,
    command,
    count_calls,
    memoize,
    repeat,
    run_command,
    safe,
    shout,
)


class TestShout:
    def test_example(self):
        @shout
        def greet(name):
            return f"hello {name}"

        assert greet("ada") == "HELLO ADA"

    def test_keyword_arguments_are_passed_on(self):
        @shout
        def greet(name, greeting="hi"):
            return f"{greeting} {name}"

        assert greet("ada", greeting="hey") == "HEY ADA"


class TestAnnounce:
    def test_prints_before_calling(self, capsys):
        @announce
        def add(a, b):
            print("adding")
            return a + b

        add(1, 2)
        assert capsys.readouterr().out == "Calling add\nadding\n"

    def test_result_is_returned(self):
        @announce
        def add(a, b):
            return a + b

        assert add(1, b=2) == 3


class TestCountCalls:
    def test_starts_at_zero(self):
        @count_calls
        def ping():
            return "pong"

        assert ping.calls == 0

    def test_counts_each_call(self):
        @count_calls
        def ping():
            return "pong"

        ping()
        ping()
        assert ping.calls == 2

    def test_result_is_returned(self):
        @count_calls
        def double(n):
            return n * 2

        assert double(4) == 8

    def test_each_function_has_its_own_count(self):
        @count_calls
        def first():
            pass

        @count_calls
        def second():
            pass

        first()
        assert second.calls == 0


class TestSafe:
    def test_returns_the_result_when_nothing_goes_wrong(self):
        @safe
        def divide(a, b):
            return a / b

        assert divide(6, 3) == 2

    def test_returns_none_on_error(self):
        @safe
        def divide(a, b):
            return a / b

        assert divide(1, 0) is None

    def test_keeps_the_name_and_docstring(self):
        @safe
        def divide(a, b):
            """Divide a by b."""
            return a / b

        assert divide.__name__ == "divide"
        assert divide.__doc__ == "Divide a by b."


class TestRepeat:
    def test_example(self):
        @repeat(3)
        def roll():
            return 4

        assert roll() == [4, 4, 4]

    def test_function_really_is_called_each_time(self):
        calls = []

        @repeat(2)
        def record(value):
            calls.append(value)
            return len(calls)

        assert record("x") == [1, 2]

    def test_zero_times(self):
        @repeat(0)
        def roll():
            return 4

        assert roll() == []


class TestMemoize:
    def test_result_is_correct(self):
        @memoize
        def square(n):
            return n * n

        assert square(4) == 16
        assert square(4) == 16

    def test_function_runs_once_per_argument(self):
        calls = []

        @memoize
        def square(n):
            calls.append(n)
            return n * n

        square(4)
        square(4)
        square(5)
        assert calls == [4, 5]

    def test_several_arguments(self):
        calls = []

        @memoize
        def add(a, b):
            calls.append((a, b))
            return a + b

        assert add(1, 2) == 3
        assert add(2, 1) == 3
        assert add(1, 2) == 3
        assert calls == [(1, 2), (2, 1)]


class TestCommand:
    @pytest.fixture(autouse=True)
    def empty_registry(self, monkeypatch):
        monkeypatch.setattr(decorators_exercises, "COMMANDS", {})

    def test_registers_and_runs(self):
        @command("greet")
        def say_hello(name):
            return f"Hello, {name}!"

        assert run_command("greet", "Ada") == "Hello, Ada!"

    def test_function_is_returned_unchanged(self):
        def say_hello(name):
            return f"Hello, {name}!"

        assert command("greet")(say_hello) is say_hello

    def test_function_is_stored_in_commands(self):
        @command("ping")
        def ping():
            return "pong"

        assert {"ping": ping} == decorators_exercises.COMMANDS

    def test_several_commands(self):
        @command("add")
        def add(a, b):
            return a + b

        @command("negate")
        def negate(n):
            return -n

        assert run_command("add", 2, 3) == 5
        assert run_command("negate", 4) == -4

    def test_unknown_command(self):
        with pytest.raises(ValueError, match="unknown command: launch"):
            run_command("launch")
