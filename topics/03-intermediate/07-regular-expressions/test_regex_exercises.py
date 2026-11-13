import pytest
from regex_exercises import (
    extract_hashtags,
    find_numbers,
    has_digit,
    is_valid_username,
    mask_emails,
    parse_duration,
    parse_time,
)


class TestHasDigit:
    def test_has_one(self):
        assert has_digit("room 101") is True

    def test_has_none(self):
        assert has_digit("no numbers here") is False

    def test_empty(self):
        assert has_digit("") is False


class TestFindNumbers:
    def test_example(self):
        assert find_numbers("Order 66 has 3 items") == [66, 3]

    def test_numbers_touching_letters(self):
        assert find_numbers("abc123def45") == [123, 45]

    def test_none(self):
        assert find_numbers("nothing to see") == []

    def test_results_are_ints(self):
        assert all(isinstance(number, int) for number in find_numbers("1 22 333"))


class TestIsValidUsername:
    @pytest.mark.parametrize("name", ["ada", "ada_99", "A1b", "x" * 16])
    def test_valid(self, name):
        assert is_valid_username(name) is True

    @pytest.mark.parametrize(
        "name",
        ["9lives", "_ada", "ab", "x" * 17, "ada lovelace", "ada!", "", "ada\n"],
    )
    def test_invalid(self, name):
        assert is_valid_username(name) is False


class TestExtractHashtags:
    def test_example(self):
        result = extract_hashtags("Learning #Python with #pytest_tips!")
        assert result == ["Python", "pytest_tips"]

    def test_none(self):
        assert extract_hashtags("no tags here") == []

    def test_hash_on_its_own_is_not_a_tag(self):
        assert extract_hashtags("issue # 5 and #real") == ["real"]


class TestParseTime:
    def test_example(self):
        assert parse_time("09:15:02") == (9, 15, 2)

    def test_latest_time(self):
        assert parse_time("23:59:59") == (23, 59, 59)

    def test_midnight(self):
        assert parse_time("00:00:00") == (0, 0, 0)

    @pytest.mark.parametrize(
        "text",
        [
            "9:15:02",
            "24:00:00",
            "12:60:00",
            "12:00:60",
            "09:15",
            " 09:15:02",
            "ab:cd:ef",
        ],
    )
    def test_invalid(self, text):
        assert parse_time(text) is None


class TestMaskEmails:
    def test_example(self):
        result = mask_emails("Write to ada@example.com today")
        assert result == "Write to ***@example.com today"

    def test_several_addresses(self):
        result = mask_emails("ada@example.com, bob.smith@mail.co.uk")
        assert result == "***@example.com, ***@mail.co.uk"

    def test_no_addresses(self):
        assert mask_emails("nothing to hide") == "nothing to hide"

    def test_name_with_dots_and_plus(self):
        assert mask_emails("a.b+news@site.org") == "***@site.org"


class TestParseDuration:
    def test_example(self):
        assert parse_duration("1h30m15s") == 5415

    @pytest.mark.parametrize(
        ("text", "seconds"),
        [("45m", 2700), ("2h", 7200), ("90s", 90), ("1h5s", 3605), ("10m30s", 630)],
    )
    def test_parts_are_optional(self, text, seconds):
        assert parse_duration(text) == seconds

    @pytest.mark.parametrize("text", ["", "abc", "30x", "5m2h", "1h 30m", "h", "15"])
    def test_invalid(self, text):
        with pytest.raises(ValueError):
            parse_duration(text)
