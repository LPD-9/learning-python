"""Error handling: cleaning up, retrying, and designing your own errors.

Implement each function so the tests in test_error_handling_exercises.py
pass. Run them with:  pytest topics/03-intermediate/04-error-handling

The exceptions topic covered catching and raising. This one is about
deciding what a program should do when things go wrong.
"""

from collections.abc import Callable
from pathlib import Path


class ConfigError(Exception):
    """Raised when a line of a config file can't be understood."""


def first_line(path: Path) -> str | None:
    """Return the first line of a text file, without its line ending.

    Return None if the file doesn't exist, and "" if it's empty. Open the
    file with a `with` block so that it's always closed.
    """
    raise NotImplementedError


def parse_config_line(line: str) -> tuple[str, str]:
    """Split a "key = value" line into (key, value), both stripped.

    Only the first "=" separates them, so the value may contain more.
    Raise ConfigError if there is no "=" or if the key is empty.

    >>> parse_config_line("host = localhost")
    ('host', 'localhost')
    """
    raise NotImplementedError


def run_with_cleanup(action: Callable[[], object], cleanup: Callable[[], None]):
    """Call action() and return its result. Always call cleanup() afterwards.

    cleanup must run whether action succeeds or raises. If action raises,
    the error must still reach the caller. There is a clause of the try
    statement for this.
    """
    raise NotImplementedError


def retry(func: Callable[[], object], attempts: int):
    """Call func until it succeeds, at most attempts times.

    Return the first successful result. If every attempt raises, let the
    error from the last attempt reach the caller. Catch Exception, which
    covers ordinary errors but not things like the user pressing Ctrl+C.
    """
    raise NotImplementedError


def first_success(funcs: list[Callable[[], object]]):
    """Call each function in turn and return the first result that works.

    Functions after the first success must not be called. If they all
    raise, or the list is empty, raise RuntimeError("all attempts failed").
    When there was a last error, chain the RuntimeError to it.
    """
    raise NotImplementedError


class ValidationError(Exception):
    """The parent of every error that validate_user can raise."""


class MissingFieldError(ValidationError):
    """A required field is absent.

    Give it an __init__ that takes the field's name, stores it as
    self.field and passes a message up to Exception.
    """


class InvalidValueError(ValidationError):
    """A field is present but its value isn't acceptable.

    Give it the same kind of __init__ as MissingFieldError.
    """


def validate_user(user: dict) -> bool:
    """Check a user record and return True if it's valid.

    - "name" and "age" must both be present, or MissingFieldError is
      raised for the first one that's missing (check name first).
    - name must be a string that isn't blank, or InvalidValueError.
    - age must be an int from 0 to 150, or InvalidValueError.

    Callers can catch ValidationError to handle every problem at once, or
    one of its children to handle a single kind.

    >>> validate_user({"name": "Ada", "age": 36})
    True
    """
    raise NotImplementedError


def ignoring(*error_types: type[Exception], log: list[str]):
    """Build a context manager that swallows the given errors. (Stretch)

    Used like this:

        problems = []
        with ignoring(ValueError, log=problems):
            int("not a number")
        # execution carries on here, and problems holds one message

    An error of one of the given types is caught, and str(error) is added
    to log. Any other error is left alone. Look up
    contextlib.contextmanager, or write a class with __enter__ and
    __exit__.
    """
    raise NotImplementedError
