import contextlib
import math

import pytest
from encapsulation_exercises import (
    BankAccount,
    Circle,
    Classroom,
    Person,
    Product,
    Temperature,
    User,
)


class TestCircle:
    def test_diameter(self):
        assert Circle(2).diameter == 4

    def test_area(self):
        assert Circle(2).area == pytest.approx(math.pi * 4)

    def test_values_follow_the_radius(self):
        circle = Circle(2)
        circle.radius = 5
        assert circle.diameter == 10
        assert circle.area == pytest.approx(math.pi * 25)

    def test_they_are_properties(self):
        assert isinstance(Circle.diameter, property)
        assert isinstance(Circle.area, property)


class TestPerson:
    def test_full_name(self):
        assert Person("Ada", "Lovelace").full_name == "Ada Lovelace"

    def test_follows_changes(self):
        person = Person("Ada", "Lovelace")
        person.last_name = "King"
        assert person.full_name == "Ada King"

    def test_cannot_be_assigned(self):
        person = Person("Ada", "Lovelace")
        with pytest.raises(AttributeError):
            person.full_name = "Grace Hopper"


class TestTemperature:
    def test_read_fahrenheit(self):
        assert Temperature(100).fahrenheit == 212
        assert Temperature(0).fahrenheit == 32

    def test_set_fahrenheit(self):
        temperature = Temperature(100)
        temperature.fahrenheit = 32
        assert temperature.celsius == 0

    def test_set_celsius(self):
        temperature = Temperature(0)
        temperature.celsius = -40
        assert temperature.fahrenheit == -40


class TestProduct:
    def test_read(self):
        product = Product("pen", 2.5)
        assert product.name == "pen"
        assert product.price == 2.5

    def test_change_price(self):
        product = Product("pen", 2.5)
        product.price = 3
        assert product.price == 3

    def test_free_is_allowed(self):
        assert Product("leaflet", 0).price == 0

    def test_negative_price_is_refused(self):
        product = Product("pen", 2.5)
        with pytest.raises(ValueError):
            product.price = -1
        assert product.price == 2.5

    def test_negative_price_is_refused_at_creation(self):
        with pytest.raises(ValueError):
            Product("pen", -1)


class TestUser:
    def test_read(self):
        user = User("ada", "ada@example.com")
        assert user.username == "ada"
        assert user.email == "ada@example.com"

    def test_username_cannot_be_changed(self):
        user = User("ada", "ada@example.com")
        with pytest.raises(AttributeError):
            user.username = "grace"
        assert user.username == "ada"

    def test_email_is_tidied_at_creation(self):
        assert User("ada", " Ada@Example.COM ").email == "ada@example.com"

    def test_email_is_tidied_when_changed(self):
        user = User("ada", "ada@example.com")
        user.email = "  NEW@Example.com"
        assert user.email == "new@example.com"

    def test_invalid_email_is_refused(self):
        user = User("ada", "ada@example.com")
        with pytest.raises(ValueError):
            user.email = "not an email"
        assert user.email == "ada@example.com"

    def test_invalid_email_is_refused_at_creation(self):
        with pytest.raises(ValueError):
            User("ada", "nope")


class TestClassroom:
    def test_starts_empty(self):
        assert len(Classroom().students) == 0

    def test_add_student(self):
        room = Classroom()
        room.add_student("Ada")
        room.add_student("Bob")
        assert list(room.students) == ["Ada", "Bob"]

    def test_duplicates_are_refused(self):
        room = Classroom()
        room.add_student("Ada")
        with pytest.raises(ValueError):
            room.add_student("Ada")

    def test_changing_the_result_does_not_change_the_classroom(self):
        room = Classroom()
        room.add_student("Ada")
        snapshot = room.students
        # Returning a tuple is a fine way to do this, and tuples can't append.
        with contextlib.suppress(AttributeError):
            snapshot.append("Mallory")
        assert list(room.students) == ["Ada"]

    def test_students_cannot_be_replaced(self):
        room = Classroom()
        with pytest.raises(AttributeError):
            room.students = ["Mallory"]

    def test_classrooms_are_independent(self):
        first, second = Classroom(), Classroom()
        first.add_student("Ada")
        assert len(second.students) == 0


class TestBankAccount:
    @pytest.fixture
    def account(self):
        return BankAccount("Ada", pin="1234", balance=100)

    def test_starting_values(self, account):
        assert account.owner == "Ada"
        assert account.balance == 100
        assert BankAccount("Bob", pin="0000").balance == 0

    def test_deposit_and_withdraw(self, account):
        account.deposit(50)
        account.withdraw(30)
        assert account.balance == 120

    def test_balance_cannot_be_assigned(self, account):
        with pytest.raises(AttributeError):
            account.balance = 1_000_000
        assert account.balance == 100

    @pytest.mark.parametrize("amount", [0, -5])
    def test_bad_deposits(self, account, amount):
        with pytest.raises(ValueError):
            account.deposit(amount)

    @pytest.mark.parametrize("amount", [0, -5, 101])
    def test_bad_withdrawals(self, account, amount):
        with pytest.raises(ValueError):
            account.withdraw(amount)
        assert account.balance == 100

    def test_history(self, account):
        account.deposit(50)
        account.withdraw(30)
        assert account.history == (("deposit", 50), ("withdraw", 30))

    def test_failed_transactions_are_not_recorded(self, account):
        with pytest.raises(ValueError):
            account.withdraw(500)
        assert account.history == ()

    def test_history_is_a_tuple(self, account):
        assert isinstance(account.history, tuple)

    def test_check_pin(self, account):
        assert account.check_pin("1234") is True
        assert account.check_pin("0000") is False

    def test_pin_is_name_mangled(self, account):
        assert not hasattr(account, "pin")
        assert "_BankAccount__pin" in vars(account)
