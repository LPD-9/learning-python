"""Decorators: functions that wrap other functions to add behaviour.

Implement each one so the tests in test_decorators_exercises.py pass.
Run them with:  pytest topics/03-intermediate/06-decorators

A decorator takes a function and returns a replacement for it. Writing

    @shout
    def greet(name): ...

means exactly the same as writing `greet = shout(greet)` after the
function. Everything here builds on closures, from the variable scope
topic.
"""

from collections.abc import Callable

COMMANDS: dict[str, Callable] = {}


def shout(func: Callable[..., str]) -> Callable[..., str]:
    """Make a function return its result in capitals.

    Your wrapper must accept whatever arguments the original takes and
    pass them on.

    >>> @shout
    ... def greet(name):
    ...     return f"hello {name}"
    >>> greet("ada")
    'HELLO ADA'
    """
    raise NotImplementedError


def announce(func: Callable) -> Callable:
    """Print "Calling NAME" before each call, where NAME is the function's name.

    The call must still happen, with all its positional and keyword
    arguments, and its result must still be returned.
    """
    raise NotImplementedError


def count_calls(func: Callable) -> Callable:
    """Count how many times the function has been called.

    Store the count on the wrapper as an attribute called `calls`.
    Functions are objects, so they can have attributes.

    >>> @count_calls
    ... def ping():
    ...     return "pong"
    >>> ping()
    'pong'
    >>> ping.calls
    1
    """
    raise NotImplementedError


def safe(func: Callable) -> Callable:
    """Make a function return None instead of raising an error.

    The wrapped function must keep the original's __name__ and __doc__.
    By default a wrapper hides them. The functools module has a tool that
    fixes this, and you should use it in every decorator from now on.
    """
    raise NotImplementedError


def repeat(times: int) -> Callable[[Callable], Callable]:
    """Call the function several times and return a list of the results.

    This decorator takes an argument, so it needs one more layer:
    repeat(3) must return a decorator.

    >>> @repeat(3)
    ... def roll():
    ...     return 4
    >>> roll()
    [4, 4, 4]
    """
    raise NotImplementedError


def memoize(func: Callable) -> Callable:
    """Remember results, so the function runs once for each set of arguments.

    Keep a dict from arguments to results. You only need to support
    positional arguments. When this works, read about functools.cache,
    which does the same job.
    """
    raise NotImplementedError


def command(name: str) -> Callable[[Callable], Callable]:
    """Register a function in COMMANDS under the given name. (Stretch)

    The function itself is returned unchanged. Web frameworks and
    command-line tools use this pattern to collect handlers.

        @command("greet")
        def say_hello(name):
            return f"Hello, {name}!"

        run_command("greet", "Ada")   # 'Hello, Ada!'
    """
    raise NotImplementedError


def run_command(name: str, *args: object) -> object:
    """Call the function registered under name, passing args to it.

    Raise ValueError("unknown command: NAME") if nothing is registered.
    This is the second half of the stretch exercise.
    """
    raise NotImplementedError
