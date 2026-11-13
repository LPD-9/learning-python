from sets_exercises import (
    compare_lists,
    first_repeat,
    has_duplicates,
    is_pangram,
    missing_numbers,
    shared_interests,
    unique_visitors_per_day,
)


class TestHasDuplicates:
    def test_example(self):
        assert has_duplicates([1, 2, 3, 2])

    def test_no_duplicates(self):
        assert not has_duplicates(["a", "b", "c"])

    def test_empty(self):
        assert not has_duplicates([])


class TestIsPangram:
    def test_example(self):
        assert is_pangram("The quick brown fox jumps over the lazy dog")

    def test_missing_a_letter(self):
        assert not is_pangram("The quick brown fox jumps over the lay dog")

    def test_ignores_case_and_punctuation(self):
        assert is_pangram("ABCDEFGHIJKLM, nopqrstuvwxyz!")

    def test_empty(self):
        assert not is_pangram("")


class TestCompareLists:
    def test_example(self):
        assert compare_lists([1, 2, 3], [2, 3, 4]) == {
            "both": {2, 3},
            "only_first": {1},
            "only_second": {4},
        }

    def test_duplicates_ignored(self):
        result = compare_lists(["a", "a", "b"], ["b", "b"])
        assert result == {"both": {"b"}, "only_first": {"a"}, "only_second": set()}

    def test_empty(self):
        expected = {"both": set(), "only_first": set(), "only_second": set()}
        assert compare_lists([], []) == expected


class TestMissingNumbers:
    def test_example(self):
        assert missing_numbers([1, 2, 4, 7], 1, 7) == [3, 5, 6]

    def test_nothing_missing(self):
        assert missing_numbers([3, 1, 2], 1, 3) == []

    def test_everything_missing(self):
        assert missing_numbers([], 5, 7) == [5, 6, 7]

    def test_numbers_outside_range_ignored(self):
        assert missing_numbers([0, 2, 99], 1, 3) == [1, 3]


class TestFirstRepeat:
    def test_example(self):
        assert first_repeat(["a", "b", "b", "a"]) == "b"

    def test_repeat_later(self):
        assert first_repeat([1, 2, 3, 1]) == 1

    def test_no_repeat(self):
        assert first_repeat([1, 2, 3]) is None

    def test_empty(self):
        assert first_repeat([]) is None


class TestSharedInterests:
    def test_example(self):
        people = {"ann": {"chess", "golf"}, "ben": {"golf", "jazz"}}
        assert shared_interests(people) == {"golf"}

    def test_three_people(self):
        people = {
            "ann": {"chess", "golf", "jazz"},
            "ben": {"golf", "jazz"},
            "cat": {"jazz", "golf", "tennis"},
        }
        assert shared_interests(people) == {"golf", "jazz"}

    def test_nothing_in_common(self):
        assert shared_interests({"ann": {"chess"}, "ben": {"golf"}}) == set()

    def test_one_person(self):
        assert shared_interests({"ann": {"chess", "golf"}}) == {"chess", "golf"}

    def test_no_people(self):
        assert shared_interests({}) == set()

    def test_inputs_are_not_modified(self):
        people = {"ann": {"chess", "golf"}, "ben": {"golf"}}
        shared_interests(people)
        assert people == {"ann": {"chess", "golf"}, "ben": {"golf"}}


class TestUniqueVisitorsPerDay:
    def test_example(self):
        visits = [("mon", "ann"), ("mon", "ann"), ("tue", "ann")]
        assert unique_visitors_per_day(visits) == {"mon": 1, "tue": 1}

    def test_several_users(self):
        visits = [
            ("mon", "ann"),
            ("mon", "ben"),
            ("mon", "ann"),
            ("tue", "cat"),
        ]
        assert unique_visitors_per_day(visits) == {"mon": 2, "tue": 1}

    def test_empty(self):
        assert unique_visitors_per_day([]) == {}
