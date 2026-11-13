import pytest
from tuples_exercises import (
    Color,
    count_friendships,
    distance,
    head_and_tail,
    min_max,
    parse_hex_color,
    rank_players,
)


class TestMinMax:
    def test_example(self):
        assert min_max([3, 9, 1]) == (1, 9)

    def test_single(self):
        assert min_max([4]) == (4, 4)

    def test_returns_a_tuple(self):
        assert isinstance(min_max([1, 2]), tuple)

    def test_empty(self):
        with pytest.raises(ValueError):
            min_max([])


class TestDistance:
    def test_example(self):
        assert distance((0, 0), (3, 4)) == 5.0

    def test_same_point(self):
        assert distance((2, 2), (2, 2)) == 0.0

    def test_negative_coordinates(self):
        assert distance((-1, -1), (2, 3)) == 5.0


class TestHeadAndTail:
    def test_example(self):
        assert head_and_tail((1, 2, 3)) == (1, (2, 3))

    def test_single_item(self):
        assert head_and_tail(("only",)) == ("only", ())

    def test_tail_is_a_tuple(self):
        _, tail = head_and_tail((1, 2, 3))
        assert isinstance(tail, tuple)

    def test_empty(self):
        with pytest.raises(ValueError):
            head_and_tail(())


class TestRankPlayers:
    def test_example(self):
        result = rank_players([("cat", 5), ("ann", 9), ("bob", 5)])
        assert result == [("ann", 9), ("bob", 5), ("cat", 5)]

    def test_empty(self):
        assert rank_players([]) == []

    def test_original_unchanged(self):
        scores = [("b", 1), ("a", 2)]
        rank_players(scores)
        assert scores == [("b", 1), ("a", 2)]


class TestParseHexColor:
    def test_example(self):
        assert parse_hex_color("#ff8000") == Color(red=255, green=128, blue=0)

    def test_uppercase(self):
        assert parse_hex_color("#00FF7F") == Color(0, 255, 127)

    def test_returns_a_color(self):
        color = parse_hex_color("#102030")
        assert isinstance(color, Color)
        assert color.green == 32


class TestCountFriendships:
    def test_example(self):
        pairs = [("ben", "ann"), ("ann", "ben"), ("ann", "cat")]
        assert count_friendships(pairs) == {("ann", "ben"): 2, ("ann", "cat"): 1}

    def test_empty(self):
        assert count_friendships([]) == {}

    def test_keys_are_sorted_tuples(self):
        assert list(count_friendships([("zoe", "amy")])) == [("amy", "zoe")]
