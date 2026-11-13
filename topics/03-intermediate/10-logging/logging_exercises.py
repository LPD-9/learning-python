"""Logging: recording what a program did, instead of printing it.

Implement each function so the tests in test_logging_exercises.py pass.
Run them with:  pytest topics/03-intermediate/10-logging

print() is for talking to the person using the program. Logging is for
whoever has to work out later what the program did. Each message has a
level (DEBUG, INFO, WARNING, ERROR, CRITICAL), so they can be filtered,
and messages can be sent to a file without changing the code that logs.

Use the logger defined below for exercises 1 to 6. Don't call print.
"""

import logging
from pathlib import Path

logger = logging.getLogger(__name__)


def greet(name: str) -> str:
    """Log "Greeting NAME" at INFO level, then return "Hello, NAME!"."""
    raise NotImplementedError


def divide(a: float, b: float) -> float | None:
    """Return a divided by b.

    If b is zero, log "Cannot divide A by zero" at ERROR level, with a's
    value in place of A, and return None.
    """
    raise NotImplementedError


def level_for_status(status: int) -> int:
    """Return the logging level that suits an HTTP status code.

    Below 400 is logging.INFO. From 400 to 499 is logging.WARNING.
    500 and above is logging.ERROR. Levels are plain ints: compare
    logging.INFO and logging.ERROR in the REPL.
    """
    raise NotImplementedError


def log_request(method: str, path: str, status: int) -> None:
    """Log a web request as "METHOD PATH -> STATUS", e.g. "GET /home -> 200".

    Use the level that level_for_status gives for the status. The logger
    has a method that takes the level as an argument.

    Pass the values as extra arguments, logger.info("%s items", count),
    instead of building the string yourself. The logging module then only
    does the formatting if the message is going to be shown.
    """
    raise NotImplementedError


def process_orders(orders: list[dict]) -> int:
    """Count the valid orders, logging as you go, and return the count.

    Each order is a dict with "id" and "quantity". An order with a
    quantity of zero or less is skipped, with a WARNING:
    "Skipping order ID: bad quantity". When every order has been looked
    at, log "Processed N of M orders" at INFO level.
    """
    raise NotImplementedError


def load_number(text: str) -> int | None:
    """Convert text to an int, or log the failure and return None.

    On failure, log "Could not parse TEXT" so that the record includes
    the full traceback. One logger method does this for you when it's
    called inside an except block.
    """
    raise NotImplementedError


def make_logger(name: str, log_file: Path) -> logging.Logger:
    """Return a logger that writes to a file. (Stretch)

    - It handles every level from DEBUG up.
    - Each message is written to log_file as "LEVEL:NAME:MESSAGE", for
      example "INFO:orders:started".
    - Calling make_logger twice with the same name must not make
      messages appear twice. Loggers are shared by name, so check
      whether this one already has a handler.

    You'll need a Handler and a Formatter.
    """
    raise NotImplementedError
