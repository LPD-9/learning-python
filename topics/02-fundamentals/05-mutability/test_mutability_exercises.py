from mutability_exercises import (
    add_bonus,
    clone_config,
    freeze,
    make_grid,
    remove_short_words,
    with_item,
)


class TestWithItem:
    def test_example(self):
        assert with_item([1, 2], 3) == [1, 2, 3]

    def test_original_unchanged(self):
        original = [1, 2]
        with_item(original, 3)
        assert original == [1, 2]

    def test_returns_a_different_list(self):
        original = [1]
        assert with_item(original, 2) is not original


class TestMakeGrid:
    def test_example(self):
        assert make_grid(2, 3) == [[0, 0, 0], [0, 0, 0]]

    def test_custom_fill(self):
        assert make_grid(1, 2, ".") == [[".", "."]]

    def test_rows_are_independent(self):
        grid = make_grid(3, 3)
        grid[0][0] = "X"
        assert grid[1][0] == 0
        assert grid[2][0] == 0

    def test_empty(self):
        assert make_grid(0, 5) == []


class TestAddBonus:
    def test_example(self):
        assert add_bonus({"ann": 5, "ben": 7}, 2) == {"ann": 7, "ben": 9}

    def test_original_unchanged(self):
        scores = {"ann": 5}
        add_bonus(scores, 10)
        assert scores == {"ann": 5}


class TestCloneConfig:
    def test_equal_to_original(self):
        config = {"db": {"hosts": ["a", "b"]}, "debug": True}
        assert clone_config(config) == config

    def test_top_level_change_is_independent(self):
        config = {"debug": True}
        copy = clone_config(config)
        copy["debug"] = False
        assert config["debug"] is True

    def test_deeply_nested_change_is_independent(self):
        config = {"db": {"hosts": ["a", "b"]}}
        copy = clone_config(config)
        copy["db"]["hosts"].append("c")
        assert config == {"db": {"hosts": ["a", "b"]}}


class TestRemoveShortWords:
    def test_example(self):
        words = ["a", "to", "cat", "be", "horse"]
        remove_short_words(words, 3)
        assert words == ["cat", "horse"]

    def test_short_words_next_to_each_other(self):
        words = ["a", "b", "c", "dog"]
        remove_short_words(words, 2)
        assert words == ["dog"]

    def test_returns_none(self):
        assert remove_short_words(["a"], 2) is None

    def test_modifies_the_same_list(self):
        words = ["a", "cat"]
        alias = words
        remove_short_words(words, 2)
        assert alias == ["cat"]


class TestFreeze:
    def test_example(self):
        assert freeze({"b": [1, 2], "a": {3}}) == (
            ("a", frozenset({3})),
            ("b", (1, 2)),
        )

    def test_nested_lists(self):
        assert freeze([1, [2, [3]]]) == (1, (2, (3,)))

    def test_plain_values_unchanged(self):
        assert freeze(5) == 5
        assert freeze("text") == "text"

    def test_result_is_hashable(self):
        frozen = freeze({"tags": ["x", "y"], "meta": {"ids": {1, 2}}})
        hash(frozen)  # raises TypeError if anything mutable is left inside

    def test_can_be_used_as_a_dict_key(self):
        cache = {freeze({"page": 1, "filters": ["new"]}): "result"}
        assert cache[freeze({"filters": ["new"], "page": 1})] == "result"
