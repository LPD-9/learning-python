from collections.abc import Callable
from typing import get_type_hints

from type_annotations_exercises import (
    Movie,
    add_tax,
    apply_to_all,
    describe_movie,
    find_age,
    first_or,
    shout_all,
    tally,
)


class TestAddTax:
    def test_behaviour(self):
        assert add_tax(100.0, 0.2) == 120.0
        assert add_tax(50.0, 0.0) == 50.0

    def test_annotations(self):
        assert get_type_hints(add_tax) == {
            "price": float,
            "rate": float,
            "return": float,
        }


class TestShoutAll:
    def test_behaviour(self):
        assert shout_all(["hi", "there"]) == ["HI", "THERE"]
        assert shout_all([]) == []

    def test_annotations(self):
        assert get_type_hints(shout_all) == {
            "words": list[str],
            "return": list[str],
        }


class TestTally:
    def test_behaviour(self):
        assert tally(["a", "b", "a"]) == {"a": 2, "b": 1}
        assert tally([]) == {}

    def test_annotations(self):
        assert get_type_hints(tally) == {
            "items": list[str],
            "return": dict[str, int],
        }


class TestFindAge:
    def test_behaviour(self):
        assert find_age({"ada": 36}, "ada") == 36
        assert find_age({"ada": 36}, "bob") is None

    def test_age_of_zero_is_still_returned(self):
        assert find_age({"baby": 0}, "baby") == 0

    def test_annotations(self):
        assert get_type_hints(find_age) == {
            "ages": dict[str, int],
            "name": str,
            "return": int | None,
        }


class TestApplyToAll:
    def test_behaviour(self):
        assert apply_to_all(abs, [-1, 2, -3]) == [1, 2, 3]
        assert apply_to_all(lambda n: n * 2, [1, 2]) == [2, 4]
        assert apply_to_all(abs, []) == []

    def test_annotations(self):
        assert get_type_hints(apply_to_all) == {
            "func": Callable[[int], int],
            "numbers": list[int],
            "return": list[int],
        }


class TestMovie:
    def test_keys_and_types(self):
        assert get_type_hints(Movie) == {"title": str, "year": int}

    def test_describe_behaviour(self):
        assert describe_movie({"title": "Alien", "year": 1979}) == "Alien (1979)"

    def test_describe_annotations(self):
        assert get_type_hints(describe_movie) == {"movie": Movie, "return": str}


class TestFirstOr:
    def test_behaviour(self):
        assert first_or([4, 5], 0) == 4
        assert first_or([], "none") == "none"

    def test_a_falsy_first_item_is_still_returned(self):
        assert first_or([0, 5], 9) == 0

    def test_is_generic(self):
        type_params = first_or.__type_params__
        assert len(type_params) == 1, "write it as: def first_or[T](...)"

    def test_annotations(self):
        type_params = first_or.__type_params__
        assert len(type_params) == 1, "write it as: def first_or[T](...)"
        t = type_params[0]
        assert get_type_hints(first_or) == {
            "items": list[t],
            "default": t,
            "return": t,
        }
