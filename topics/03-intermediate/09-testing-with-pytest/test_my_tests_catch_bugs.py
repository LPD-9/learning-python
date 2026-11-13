"""Checks the tests you wrote in test_testing_exercises.py. Don't edit this.

It makes broken copies of testing_exercises.py, each with one small bug,
and runs your tests against every copy in a scratch folder. If your tests
still pass when the code is broken, they aren't checking enough.
"""

import subprocess
import sys
from pathlib import Path

import pytest
from testing_bugs import BUGS

HERE = Path(__file__).parent
CODE = (HERE / "testing_exercises.py").read_text(encoding="utf-8")
MY_TESTS = HERE / "test_testing_exercises.py"

NO_TESTS_COLLECTED = 5


def run_my_tests(folder: Path, code: str) -> subprocess.CompletedProcess[str]:
    """Run your tests against one version of the code, in its own folder."""
    my_tests = MY_TESTS.read_text(encoding="utf-8")
    (folder / "testing_exercises.py").write_text(code, encoding="utf-8")
    (folder / MY_TESTS.name).write_text(my_tests, encoding="utf-8")
    (folder / "pytest.ini").write_text("[pytest]\n", encoding="utf-8")
    return subprocess.run(
        [sys.executable, "-m", "pytest", MY_TESTS.name, "-q", "-x", "--tb=short"],
        cwd=folder,
        capture_output=True,
        text=True,
        check=False,
    )


@pytest.fixture(scope="module")
def result_on_correct_code(tmp_path_factory):
    return run_my_tests(tmp_path_factory.mktemp("correct"), CODE)


def fail(message: str) -> None:
    """Fail the test with a plain message and no traceback."""
    pytest.fail(message, pytrace=False)


def test_my_tests_pass_on_the_correct_code(result_on_correct_code):
    result = result_on_correct_code
    if result.returncode == NO_TESTS_COLLECTED:
        fail("No tests found yet. Write some in test_testing_exercises.py.")
    if result.returncode != 0:
        fail("Your tests must pass on the unbroken code first:\n" + result.stdout)


def my_tests_use(decorator: str) -> bool:
    """Return True if a line of your test file starts with the decorator."""
    lines = MY_TESTS.read_text(encoding="utf-8").splitlines()
    return any(line.strip().startswith(decorator) for line in lines)


def test_my_tests_use_parametrize():
    if not my_tests_use("@pytest.mark.parametrize"):
        fail("None of your tests use @pytest.mark.parametrize yet (exercise 4).")


def test_my_tests_use_a_fixture():
    if not my_tests_use("@pytest.fixture"):
        fail("You haven't written a fixture with @pytest.fixture yet (exercise 5).")


@pytest.mark.parametrize(
    ("function", "hint", "original", "broken"),
    BUGS,
    ids=[f"{bug[0]}-bug-{number}" for number, bug in enumerate(BUGS, start=1)],
)
def test_bug_is_caught(
    function, hint, original, broken, result_on_correct_code, tmp_path
):
    if result_on_correct_code.returncode != 0:
        fail("Get your tests passing on the unbroken code first.")
    if CODE.count(original) != 1:
        fail("testing_exercises.py has been edited. Please restore it.")

    result = run_my_tests(tmp_path, CODE.replace(original, broken))

    if result.returncode != 1:
        fail(
            f"A bug was planted in {function} and none of your tests noticed. "
            f"Hint: test {hint}."
        )
