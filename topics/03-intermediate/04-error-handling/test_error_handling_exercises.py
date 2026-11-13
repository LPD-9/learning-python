import pytest
from error_handling_exercises import (
    ConfigError,
    InvalidValueError,
    MissingFieldError,
    ValidationError,
    first_line,
    first_success,
    ignoring,
    parse_config_line,
    retry,
    run_with_cleanup,
    validate_user,
)


def fail_then_succeed(failures, result="done"):
    """Return a function that raises ValueError a set number of times first."""
    calls = []

    def flaky():
        calls.append(1)
        if len(calls) <= failures:
            raise ValueError(f"attempt {len(calls)} failed")
        return result

    flaky.calls = calls
    return flaky


class TestFirstLine:
    def test_reads_the_first_line(self, tmp_path):
        file = tmp_path / "notes.txt"
        file.write_text("first\nsecond\n", encoding="utf-8")
        assert first_line(file) == "first"

    def test_single_line_without_a_line_ending(self, tmp_path):
        file = tmp_path / "notes.txt"
        file.write_text("only", encoding="utf-8")
        assert first_line(file) == "only"

    def test_empty_file(self, tmp_path):
        file = tmp_path / "empty.txt"
        file.write_text("", encoding="utf-8")
        assert first_line(file) == ""

    def test_missing_file(self, tmp_path):
        assert first_line(tmp_path / "nowhere.txt") is None


class TestParseConfigLine:
    def test_example(self):
        assert parse_config_line("host = localhost") == ("host", "localhost")

    def test_no_spaces(self):
        assert parse_config_line("port=8080") == ("port", "8080")

    def test_value_contains_equals(self):
        assert parse_config_line("query = a=1&b=2") == ("query", "a=1&b=2")

    def test_empty_value_is_allowed(self):
        assert parse_config_line("password =") == ("password", "")

    def test_no_equals(self):
        with pytest.raises(ConfigError):
            parse_config_line("just some words")

    def test_empty_key(self):
        with pytest.raises(ConfigError):
            parse_config_line(" = value")


class TestRunWithCleanup:
    def test_returns_the_result(self):
        assert run_with_cleanup(lambda: 42, lambda: None) == 42

    def test_cleanup_runs_after_success(self):
        events = []
        run_with_cleanup(
            lambda: events.append("action"), lambda: events.append("clean")
        )
        assert events == ["action", "clean"]

    def test_cleanup_runs_after_an_error(self):
        events = []

        def explode():
            raise KeyError("boom")

        with pytest.raises(KeyError):
            run_with_cleanup(explode, lambda: events.append("clean"))
        assert events == ["clean"]


class TestRetry:
    def test_succeeds_first_time(self):
        func = fail_then_succeed(0)
        assert retry(func, attempts=3) == "done"
        assert len(func.calls) == 1

    def test_succeeds_after_failures(self):
        func = fail_then_succeed(2)
        assert retry(func, attempts=3) == "done"
        assert len(func.calls) == 3

    def test_gives_up_and_raises_the_last_error(self):
        func = fail_then_succeed(5)
        with pytest.raises(ValueError, match="attempt 3 failed"):
            retry(func, attempts=3)
        assert len(func.calls) == 3


class TestFirstSuccess:
    def test_first_one_works(self):
        assert first_success([lambda: "a", lambda: "b"]) == "a"

    def test_skips_failures(self):
        assert first_success([fail_then_succeed(1), lambda: "backup"]) == "backup"

    def test_later_functions_are_not_called(self):
        never = fail_then_succeed(0)
        first_success([lambda: "a", never])
        assert never.calls == []

    def test_all_fail(self):
        with pytest.raises(RuntimeError, match="all attempts failed") as error:
            first_success([fail_then_succeed(1), fail_then_succeed(1)])
        assert isinstance(error.value.__cause__, ValueError)

    def test_empty(self):
        with pytest.raises(RuntimeError, match="all attempts failed"):
            first_success([])


class TestValidateUser:
    def test_valid(self):
        assert validate_user({"name": "Ada", "age": 36}) is True

    def test_missing_name(self):
        with pytest.raises(MissingFieldError) as error:
            validate_user({"age": 36})
        assert error.value.field == "name"

    def test_missing_age(self):
        with pytest.raises(MissingFieldError) as error:
            validate_user({"name": "Ada"})
        assert error.value.field == "age"

    def test_blank_name(self):
        with pytest.raises(InvalidValueError) as error:
            validate_user({"name": "   ", "age": 36})
        assert error.value.field == "name"

    def test_age_out_of_range(self):
        with pytest.raises(InvalidValueError) as error:
            validate_user({"name": "Ada", "age": 200})
        assert error.value.field == "age"

    def test_age_is_not_a_number(self):
        with pytest.raises(InvalidValueError):
            validate_user({"name": "Ada", "age": "36"})

    def test_parent_class_catches_both_kinds(self):
        with pytest.raises(ValidationError):
            validate_user({})
        with pytest.raises(ValidationError):
            validate_user({"name": "Ada", "age": -1})

    def test_errors_have_messages(self):
        with pytest.raises(MissingFieldError) as error:
            validate_user({})
        assert str(error.value) != ""


class TestIgnoring:
    def test_listed_error_is_swallowed(self):
        problems = []
        with ignoring(ValueError, log=problems):
            int("not a number")
        assert len(problems) == 1
        assert "not a number" in problems[0]

    def test_code_after_the_block_runs(self):
        reached = []
        with ignoring(ZeroDivisionError, log=[]):
            1 / 0  # noqa: B018
        reached.append(True)
        assert reached == [True]

    def test_several_error_types(self):
        problems = []
        with ignoring(ValueError, KeyError, log=problems):
            {}["missing"]
        assert len(problems) == 1

    def test_other_errors_are_not_swallowed(self):
        problems = []
        with pytest.raises(KeyError), ignoring(ValueError, log=problems):
            {}["missing"]
        assert problems == []

    def test_nothing_logged_when_nothing_goes_wrong(self):
        problems = []
        with ignoring(ValueError, log=problems):
            int("5")
        assert problems == []
