from strings_exercises import (
    caesar_shift,
    format_row,
    initials,
    is_palindrome,
    normalise_name,
    parse_log_line,
    truncate,
)


class TestNormaliseName:
    def test_strips_and_capitalises(self):
        assert normalise_name("  ada   lovelace ") == "Ada Lovelace"

    def test_already_tidy(self):
        assert normalise_name("Grace Hopper") == "Grace Hopper"

    def test_tabs_and_newlines_count_as_whitespace(self):
        assert normalise_name("alan\t\tturing\n") == "Alan Turing"

    def test_empty_string(self):
        assert normalise_name("   ") == ""


class TestInitials:
    def test_example(self):
        assert initials("grace  brewster hopper") == "G.B.H."

    def test_single_name(self):
        assert initials("Cher") == "C."

    def test_extra_whitespace(self):
        assert initials("  ada lovelace ") == "A.L."

    def test_empty(self):
        assert initials("") == ""


class TestIsPalindrome:
    def test_simple(self):
        assert is_palindrome("racecar")

    def test_ignores_case_and_punctuation(self):
        assert is_palindrome("A man, a plan, a canal: Panama")

    def test_not_a_palindrome(self):
        assert not is_palindrome("python")

    def test_digits_count(self):
        assert is_palindrome("12321")
        assert not is_palindrome("123")

    def test_empty_string_is_a_palindrome(self):
        assert is_palindrome("")


class TestTruncate:
    def test_example(self):
        assert truncate("Hello, world", 8) == "Hello..."

    def test_fits_already(self):
        assert truncate("Hi", 5) == "Hi"

    def test_exact_length_is_unchanged(self):
        assert truncate("Hello", 5) == "Hello"

    def test_result_length(self):
        assert len(truncate("a" * 100, 10)) == 10

    def test_minimum_length(self):
        assert truncate("Hello", 3) == "..."


class TestParseLogLine:
    def test_example(self):
        assert parse_log_line("2026-10-30 09:15:02 ERROR Disk is full") == (
            "2026-10-30 09:15:02",
            "ERROR",
            "Disk is full",
        )

    def test_single_word_message(self):
        assert parse_log_line("2026-01-01 00:00:00 INFO Started") == (
            "2026-01-01 00:00:00",
            "INFO",
            "Started",
        )

    def test_returns_a_tuple(self):
        result = parse_log_line("2026-01-01 00:00:00 INFO Started")
        assert isinstance(result, tuple)


class TestFormatRow:
    def test_example(self):
        assert format_row(["id", "name"], [4, 6]) == "| id   | name   |"

    def test_cell_exactly_fills_width(self):
        assert format_row(["abc"], [3]) == "| abc |"

    def test_three_columns(self):
        assert format_row(["1", "Ada", "UK"], [2, 5, 3]) == "| 1  | Ada   | UK  |"


class TestCaesarShift:
    def test_example(self):
        assert caesar_shift("Hello, World!", 3) == "Khoor, Zruog!"

    def test_wraps_around(self):
        assert caesar_shift("xyz", 3) == "abc"
        assert caesar_shift("XYZ", 3) == "ABC"

    def test_negative_shift(self):
        assert caesar_shift("abc", -1) == "zab"

    def test_large_shift(self):
        assert caesar_shift("abc", 27) == "bcd"

    def test_round_trip(self):
        assert caesar_shift(caesar_shift("Secret msg 42", 11), -11) == "Secret msg 42"
