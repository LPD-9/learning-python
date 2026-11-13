from dictionaries_exercises import (
    count_words,
    get_nested,
    invert_roles,
    merge_inventories,
    rename_keys,
    top_n,
)


class TestCountWords:
    def test_example(self):
        assert count_words("The cat. The hat!") == {"the": 2, "cat": 1, "hat": 1}

    def test_extra_whitespace(self):
        assert count_words("  one   two\none ") == {"one": 2, "two": 1}

    def test_inner_punctuation_is_kept(self):
        assert count_words("don't stop") == {"don't": 1, "stop": 1}

    def test_empty(self):
        assert count_words("") == {}


class TestRenameKeys:
    def test_example(self):
        result = rename_keys({"fname": "Ada", "age": 36}, {"fname": "first_name"})
        assert result == {"first_name": "Ada", "age": 36}

    def test_rename_not_in_record_is_ignored(self):
        assert rename_keys({"a": 1}, {"z": "zz"}) == {"a": 1}

    def test_original_unchanged(self):
        record = {"fname": "Ada"}
        rename_keys(record, {"fname": "first_name"})
        assert record == {"fname": "Ada"}


class TestInvertRoles:
    def test_example(self):
        result = invert_roles({"bob": "user", "alice": "admin", "carol": "admin"})
        assert result == {"user": ["bob"], "admin": ["alice", "carol"]}

    def test_users_are_sorted(self):
        result = invert_roles({"zoe": "admin", "adam": "admin"})
        assert result == {"admin": ["adam", "zoe"]}

    def test_empty(self):
        assert invert_roles({}) == {}


class TestTopN:
    def test_example(self):
        assert top_n({"a": 1, "b": 5, "c": 3, "d": 5}, 3) == ["b", "d", "c"]

    def test_n_bigger_than_dict(self):
        assert top_n({"x": 1, "y": 2}, 10) == ["y", "x"]

    def test_zero(self):
        assert top_n({"x": 1}, 0) == []


class TestMergeInventories:
    def test_example(self):
        result = merge_inventories({"apple": 3, "pear": 1}, {"apple": 2, "pear": -1})
        assert result == {"apple": 5}

    def test_items_only_in_one_inventory(self):
        result = merge_inventories({"apple": 1}, {"kiwi": 4})
        assert result == {"apple": 1, "kiwi": 4}

    def test_negative_totals_are_dropped(self):
        assert merge_inventories({"fig": 1}, {"fig": -5}) == {}

    def test_inputs_are_not_modified(self):
        first = {"apple": 3}
        second = {"apple": 2, "kiwi": 1}
        merge_inventories(first, second)
        assert first == {"apple": 3}
        assert second == {"apple": 2, "kiwi": 1}


CONFIG = {"db": {"host": "localhost", "port": 5432}, "debug": False}


class TestGetNested:
    def test_nested_value(self):
        assert get_nested(CONFIG, "db.port") == 5432

    def test_top_level_value(self):
        assert get_nested(CONFIG, "debug") is False

    def test_missing_with_default(self):
        assert get_nested(CONFIG, "db.user", "admin") == "admin"

    def test_missing_without_default(self):
        assert get_nested(CONFIG, "cache.size") is None

    def test_path_goes_through_a_non_dict(self):
        assert get_nested(CONFIG, "db.port.number", "n/a") == "n/a"

    def test_whole_sub_dict(self):
        assert get_nested(CONFIG, "db") == {"host": "localhost", "port": 5432}
