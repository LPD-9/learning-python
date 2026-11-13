import pytest
import scope_exercises
from scope_exercises import (
    apply_discount,
    make_account,
    make_accumulator,
    make_greeter,
    make_multipliers,
    next_ticket_number,
    register_plugin,
)


class TestApplyDiscount:
    def test_example(self):
        assert apply_discount(200) == pytest.approx(180)

    def test_follows_the_constant(self, monkeypatch):
        monkeypatch.setattr(scope_exercises, "DISCOUNT_RATE", 0.5)
        assert apply_discount(200) == pytest.approx(100)

    def test_does_not_change_the_constant(self):
        before = scope_exercises.DISCOUNT_RATE
        apply_discount(50)
        assert before == scope_exercises.DISCOUNT_RATE


class TestRegisterPlugin:
    def test_adds_and_counts(self, monkeypatch):
        monkeypatch.setattr(scope_exercises, "PLUGINS", [])
        assert register_plugin("spellcheck") == 1
        assert register_plugin("autosave") == 2

    def test_module_list_is_changed(self, monkeypatch):
        monkeypatch.setattr(scope_exercises, "PLUGINS", ["existing"])
        register_plugin("autosave")
        assert scope_exercises.PLUGINS == ["existing", "autosave"]


class TestNextTicketNumber:
    def test_counts_up(self, monkeypatch):
        monkeypatch.setattr(scope_exercises, "_last_ticket", 0)
        assert next_ticket_number() == 1
        assert next_ticket_number() == 2

    def test_module_variable_is_updated(self, monkeypatch):
        monkeypatch.setattr(scope_exercises, "_last_ticket", 41)
        next_ticket_number()
        assert scope_exercises._last_ticket == 42


class TestMakeGreeter:
    def test_example(self):
        hello = make_greeter("Hello")
        assert hello("Ada") == "Hello, Ada!"

    def test_greeters_are_independent(self):
        hello = make_greeter("Hello")
        howdy = make_greeter("Howdy")
        assert hello("Ada") == "Hello, Ada!"
        assert howdy("Bob") == "Howdy, Bob!"


class TestMakeAccumulator:
    def test_example(self):
        add = make_accumulator(10)
        assert add(5) == 15
        assert add(2) == 17

    def test_negative_amounts(self):
        add = make_accumulator(0)
        assert add(-3) == -3

    def test_accumulators_are_independent(self):
        first = make_accumulator(0)
        second = make_accumulator(100)
        first(1)
        assert second(1) == 101
        assert first(1) == 2


class TestMakeMultipliers:
    def test_each_function_uses_its_own_number(self):
        multipliers = make_multipliers(4)
        assert [multiply(10) for multiply in multipliers] == [0, 10, 20, 30]

    def test_count(self):
        assert len(make_multipliers(5)) == 5

    def test_none(self):
        assert make_multipliers(0) == []


class TestMakeAccount:
    def test_example(self):
        deposit, get_balance = make_account(100)
        assert deposit(50) == 150
        assert get_balance() == 150

    def test_balance_before_any_deposit(self):
        _, get_balance = make_account(30)
        assert get_balance() == 30

    def test_several_deposits(self):
        deposit, get_balance = make_account(0)
        deposit(10)
        deposit(5)
        assert get_balance() == 15

    def test_accounts_are_independent(self):
        deposit_a, get_balance_a = make_account(0)
        deposit_b, get_balance_b = make_account(0)
        deposit_a(99)
        deposit_b(1)
        assert get_balance_a() == 99
        assert get_balance_b() == 1
