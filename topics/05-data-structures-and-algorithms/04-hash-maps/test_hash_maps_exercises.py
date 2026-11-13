import pytest
from hash_maps_exercises import (
    HashMap,
    LRUCache,
    are_anagrams,
    first_unique_char,
    group_anagrams,
    simple_hash,
    two_sum_fast,
)


class TestSimpleHash:
    def test_example(self):
        assert simple_hash("abc", 10) == 4

    def test_same_text_always_gives_the_same_bucket(self):
        assert simple_hash("hello", 16) == simple_hash("hello", 16)

    def test_result_is_a_valid_bucket_number(self):
        for word in ["a", "hello", "a much longer piece of text"]:
            assert 0 <= simple_hash(word, 7) < 7

    def test_anagrams_collide(self):
        assert simple_hash("listen", 100) == simple_hash("silent", 100)

    def test_empty_text(self):
        assert simple_hash("", 10) == 0


class TestTwoSumFast:
    def test_example(self):
        assert two_sum_fast([2, 7, 11, 15], 9) == (0, 1)

    def test_pair_far_apart(self):
        assert two_sum_fast([1, 20, 30, 40, 8], 9) == (0, 4)

    def test_two_equal_numbers(self):
        assert two_sum_fast([3, 5, 3], 6) == (0, 2)

    def test_number_is_not_paired_with_itself(self):
        assert two_sum_fast([5, 1], 10) is None

    def test_no_pair(self):
        assert two_sum_fast([1, 2, 3], 100) is None

    def test_empty(self):
        assert two_sum_fast([], 5) is None


class TestFirstUniqueChar:
    def test_example(self):
        assert first_unique_char("swiss") == "w"

    def test_first_character(self):
        assert first_unique_char("abcab") == "c"
        assert first_unique_char("xaabb") == "x"

    def test_none_unique(self):
        assert first_unique_char("aabb") is None

    def test_empty(self):
        assert first_unique_char("") is None


class TestAreAnagrams:
    def test_example(self):
        assert are_anagrams("Listen", "Silent") is True

    def test_spaces_are_ignored(self):
        assert are_anagrams("Dormitory", "dirty room") is True

    def test_different_letters(self):
        assert are_anagrams("abc", "abd") is False

    def test_same_letters_different_counts(self):
        assert are_anagrams("aab", "abb") is False

    def test_different_lengths(self):
        assert are_anagrams("abc", "abcc") is False


class TestGroupAnagrams:
    def test_example(self):
        words = ["eat", "tea", "tan", "ate", "nat", "bat"]
        assert group_anagrams(words) == [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

    def test_no_anagrams(self):
        assert group_anagrams(["one", "two"]) == [["one"], ["two"]]

    def test_repeated_word(self):
        assert group_anagrams(["a", "a"]) == [["a", "a"]]

    def test_empty(self):
        assert group_anagrams([]) == []


class TestHashMap:
    def test_put_and_get(self):
        ages = HashMap()
        ages.put("ada", 36)
        assert ages.get("ada") == 36

    def test_missing_key(self):
        ages = HashMap()
        assert ages.get("bob") is None
        assert ages.get("bob", 0) == 0

    def test_put_replaces(self):
        ages = HashMap()
        ages.put("ada", 36)
        ages.put("ada", 37)
        assert ages.get("ada") == 37
        assert len(ages) == 1

    def test_contains(self):
        ages = HashMap()
        ages.put("ada", 36)
        assert "ada" in ages
        assert "bob" not in ages

    def test_a_stored_none_still_counts_as_present(self):
        settings = HashMap()
        settings.put("theme", None)
        assert "theme" in settings

    def test_len(self):
        ages = HashMap()
        assert len(ages) == 0
        ages.put("ada", 36)
        ages.put("bob", 25)
        assert len(ages) == 2

    def test_remove(self):
        ages = HashMap()
        ages.put("ada", 36)
        ages.remove("ada")
        assert "ada" not in ages
        assert len(ages) == 0

    def test_remove_missing_key(self):
        with pytest.raises(KeyError):
            HashMap().remove("ada")

    def test_many_keys_in_few_buckets(self):
        squares = HashMap(bucket_count=2)
        for number in range(50):
            squares.put(number, number * number)
        assert len(squares) == 50
        assert all(squares.get(number) == number * number for number in range(50))
        squares.remove(7)
        assert squares.get(7) is None
        assert squares.get(9) == 81

    def test_maps_are_independent(self):
        first, second = HashMap(), HashMap()
        first.put("a", 1)
        assert len(second) == 0


class TestLRUCache:
    def test_get_and_put(self):
        cache = LRUCache(capacity=2)
        cache.put("a", 1)
        assert cache.get("a") == 1
        assert cache.get("missing") is None

    def test_oldest_is_thrown_out_when_full(self):
        cache = LRUCache(capacity=2)
        cache.put("a", 1)
        cache.put("b", 2)
        cache.put("c", 3)
        assert cache.get("a") is None
        assert cache.get("b") == 2
        assert cache.get("c") == 3
        assert len(cache) == 2

    def test_get_counts_as_use(self):
        cache = LRUCache(capacity=2)
        cache.put("a", 1)
        cache.put("b", 2)
        cache.get("a")
        cache.put("c", 3)
        assert cache.get("a") == 1
        assert cache.get("b") is None

    def test_updating_counts_as_use(self):
        cache = LRUCache(capacity=2)
        cache.put("a", 1)
        cache.put("b", 2)
        cache.put("a", 10)
        cache.put("c", 3)
        assert cache.get("a") == 10
        assert cache.get("b") is None

    def test_updating_does_not_grow_the_cache(self):
        cache = LRUCache(capacity=2)
        cache.put("a", 1)
        cache.put("a", 2)
        assert len(cache) == 1

    def test_capacity_of_one(self):
        cache = LRUCache(capacity=1)
        cache.put("a", 1)
        cache.put("b", 2)
        assert cache.get("a") is None
        assert cache.get("b") == 2
