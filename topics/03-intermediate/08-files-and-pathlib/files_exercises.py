"""Files and pathlib: paths, reading, writing, CSV and JSON.

Implement each function so the tests in test_files_exercises.py pass.
Run them with:  pytest topics/03-intermediate/08-files-and-pathlib

Use pathlib.Path for everything to do with paths. Pass encoding="utf-8"
whenever you open a text file, so the result is the same on every
computer. The tests give each function a temporary folder to work in.
"""

from pathlib import Path


def file_extension(filename: str) -> str:
    """Return a file's extension in lowercase, without the dot.

    Return "" if there isn't one. Path objects know their own parts.

    >>> file_extension("Report.PDF")
    'pdf'
    >>> file_extension("archive.tar.gz")
    'gz'
    """
    raise NotImplementedError


def count_lines(path: Path) -> int:
    """Return the number of lines in a text file."""
    raise NotImplementedError


def write_lines(path: Path, lines: list[str]) -> int:
    """Write each string to the file on its own line.

    Anything already in the file is replaced. Return how many lines were
    written.
    """
    raise NotImplementedError


def list_python_files(folder: Path) -> list[str]:
    """Return the names of the .py files directly inside folder, sorted.

    Files in subfolders are not included. Path has a method for finding
    files that match a pattern.
    """
    raise NotImplementedError


def read_csv_totals(path: Path) -> dict[str, float]:
    """Add up the amounts for each name in a CSV file.

    The file has a header row "name,amount" followed by one row per
    payment. A name can appear on several rows. Use the csv module: it
    has a reader that turns each row into a dict.
    """
    raise NotImplementedError


def update_json_counter(path: Path, key: str) -> int:
    """Add 1 to a counter stored in a JSON file, and return its new value.

    The file holds one JSON object that maps keys to counts. If the file
    doesn't exist, or the key isn't in it, counting starts from zero.
    Other keys in the file must be kept.
    """
    raise NotImplementedError


def organise_by_extension(folder: Path) -> dict[str, int]:
    """Sort a folder's files into subfolders by extension. (Stretch)

    Each file directly inside folder moves into a subfolder named after
    its lowercase extension without the dot. "notes.TXT" goes to "txt".
    Files with no extension go into "other". Subfolders that already
    exist are left alone, along with whatever is in them.

    Return a dict that maps each subfolder name to the number of files
    moved into it.
    """
    raise NotImplementedError
