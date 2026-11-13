from booleans_and_none_exercises import (
    apply_overrides,
    count_truthy,
    describe,
    display_name,
    first_truthy,
    is_blank,
)


class TestIsBlank:
    def test_none(self):
        assert is_blank(None)

    def test_empty(self):
        assert is_blank("")

    def test_whitespace(self):
        assert is_blank("  \t\n")

    def test_has_content(self):
        assert not is_blank("  hi  ")


class TestDescribe:
    def test_none(self):
        assert describe(None) == "none"

    def test_falsy_values(self):
        for value in [0, 0.0, "", [], {}, False]:
            assert describe(value) == "falsy", value

    def test_truthy_values(self):
        for value in [1, -1, "0", " ", [0], {"a": 1}, True]:
            assert describe(value) == "truthy", value


class TestCountTruthy:
    def test_example(self):
        assert count_truthy([0, 1, "", "a", None, [1]]) == 3

    def test_all_falsy(self):
        assert count_truthy([0, "", None, []]) == 0

    def test_empty(self):
        assert count_truthy([]) == 0


class TestFirstTruthy:
    def test_example(self):
        assert first_truthy([0, "", "hello", "world"]) == "hello"

    def test_none_found(self):
        assert first_truthy([0, "", None]) is None

    def test_empty(self):
        assert first_truthy([]) is None

    def test_returns_the_value_itself(self):
        items = [1, 2]
        assert first_truthy([[], items]) is items


class TestDisplayName:
    def test_nickname_wins(self):
        assert display_name({"nickname": "Ada", "full_name": "Ada Lovelace"}) == "Ada"

    def test_empty_nickname(self):
        user = {"nickname": "", "full_name": "Ada Lovelace"}
        assert display_name(user) == "Ada Lovelace"

    def test_none_nickname(self):
        user = {"nickname": None, "full_name": "Ada Lovelace"}
        assert display_name(user) == "Ada Lovelace"

    def test_missing_keys(self):
        assert display_name({"full_name": "Alan Turing"}) == "Alan Turing"
        assert display_name({}) == "Anonymous"

    def test_nothing_usable(self):
        assert display_name({"nickname": None, "full_name": ""}) == "Anonymous"


class TestApplyOverrides:
    def test_example(self):
        result = apply_overrides(
            {"volume": 5, "muted": True}, {"volume": 0, "muted": None}
        )
        assert result == {"volume": 0, "muted": True}

    def test_false_and_empty_string_win(self):
        result = apply_overrides(
            {"dark_mode": True, "name": "x"},
            {
                "dark_mode": False,
                "name": "",
            },
        )
        assert result == {"dark_mode": False, "name": ""}

    def test_new_keys(self):
        result = apply_overrides({"a": 1}, {"b": 2, "c": None})
        assert result == {"a": 1, "b": 2}

    def test_inputs_are_not_modified(self):
        defaults = {"a": 1}
        overrides = {"a": 2}
        apply_overrides(defaults, overrides)
        assert defaults == {"a": 1}
        assert overrides == {"a": 2}
