import pytest
from methods_exercises import Card, Duration, Money, Point, Team, Vector, Version


class TestPoint:
    def test_attributes(self):
        point = Point(1, 2)
        assert (point.x, point.y) == (1, 2)

    def test_repr(self):
        assert repr(Point(1, 2)) == "Point(x=1, y=2)"

    def test_repr_is_used_inside_lists(self):
        assert str([Point(0, 0)]) == "[Point(x=0, y=0)]"


class TestMoney:
    def test_pounds_and_pence(self):
        assert str(Money(350)) == "£3.50"

    def test_pence_only(self):
        assert str(Money(5)) == "£0.05"

    def test_whole_pounds(self):
        assert str(Money(1200)) == "£12.00"

    def test_used_by_f_strings(self):
        assert f"Total: {Money(999)}" == "Total: £9.99"


class TestCard:
    def test_equal(self):
        assert Card("A", "spades") == Card("A", "spades")

    def test_different_rank(self):
        assert Card("A", "spades") != Card("K", "spades")

    def test_different_suit(self):
        assert Card("A", "spades") != Card("A", "hearts")

    def test_not_equal_to_other_types(self):
        assert Card("A", "spades") != "A of spades"
        assert Card("A", "spades") != None  # noqa: E711

    def test_found_in_a_list(self):
        hand = [Card("2", "clubs"), Card("A", "spades")]
        assert Card("A", "spades") in hand


class TestTeam:
    def test_len(self):
        assert len(Team(["ada", "bob"])) == 2

    def test_contains(self):
        team = Team(["ada", "bob"])
        assert "ada" in team
        assert "zoe" not in team

    def test_empty_team_is_falsy(self):
        assert not Team([])
        assert Team(["ada"])


class TestDuration:
    def test_plain(self):
        assert Duration(90).seconds == 90

    def test_from_minutes(self):
        duration = Duration.from_minutes(2)
        assert isinstance(duration, Duration)
        assert duration.seconds == 120

    def test_from_text(self):
        assert Duration.from_text("1:30").seconds == 90
        assert Duration.from_text("0:05").seconds == 5
        assert Duration.from_text("12:00").seconds == 720

    @pytest.mark.parametrize("text", ["1:30", "0:00", "125:59"])
    def test_valid_text(self, text):
        assert Duration.is_valid_text(text) is True

    @pytest.mark.parametrize("text", ["1:75", "1:5", "abc", "1-30", "", ":30"])
    def test_invalid_text(self, text):
        assert Duration.is_valid_text(text) is False

    def test_static_method_works_on_an_instance_too(self):
        assert Duration(1).is_valid_text("1:30") is True


class TestVector:
    def test_equality(self):
        assert Vector(1, 2) == Vector(1, 2)
        assert Vector(1, 2) != Vector(2, 1)

    def test_add(self):
        assert Vector(1, 2) + Vector(3, 4) == Vector(4, 6)

    def test_add_returns_a_new_vector(self):
        first, second = Vector(1, 2), Vector(3, 4)
        total = first + second
        assert isinstance(total, Vector)
        assert first == Vector(1, 2)

    def test_abs_is_the_length(self):
        assert abs(Vector(3, 4)) == 5.0

    def test_adding_a_number_is_a_type_error(self):
        with pytest.raises(TypeError):
            Vector(1, 2) + 5


class TestVersion:
    def test_equal(self):
        assert Version("1.2.3") == Version("1.2.3")
        assert Version("1.2.3") != Version("1.2.4")

    def test_compares_numerically(self):
        assert Version("1.10.0") > Version("1.9.0")
        assert Version("1.9.0") < Version("1.10.0")

    def test_all_comparisons(self):
        assert Version("2.0.0") >= Version("2.0.0")
        assert Version("2.0.0") <= Version("2.0.1")
        assert not Version("2.0.0") > Version("2.0.0")

    def test_sorting(self):
        versions = [Version("1.10.0"), Version("1.2.0"), Version("1.9.3")]
        expected = [Version("1.2.0"), Version("1.9.3"), Version("1.10.0")]
        assert sorted(versions) == expected

    def test_repr(self):
        assert repr(Version("2.0.1")) == "Version('2.0.1')"

    def test_equal_versions_are_one_item_in_a_set(self):
        assert len({Version("1.0.0"), Version("1.0.0"), Version("1.0.1")}) == 2
