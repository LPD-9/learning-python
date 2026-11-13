import pytest
from classes_exercises import (
    BankAccount,
    Dog,
    Employee,
    Inventory,
    Playlist,
    Rectangle,
    Tally,
)


class TestDog:
    def test_name_is_stored(self):
        assert Dog("Rex").name == "Rex"

    def test_speak(self):
        assert Dog("Rex").speak() == "Rex says woof"

    def test_each_dog_has_its_own_name(self):
        rex, fido = Dog("Rex"), Dog("Fido")
        assert rex.speak() == "Rex says woof"
        assert fido.speak() == "Fido says woof"


class TestRectangle:
    def test_attributes(self):
        page = Rectangle(3, 4)
        assert (page.width, page.height) == (3, 4)

    def test_area(self):
        assert Rectangle(3, 4).area() == 12

    def test_perimeter(self):
        assert Rectangle(3, 4).perimeter() == 14

    def test_changing_an_attribute_changes_the_area(self):
        page = Rectangle(3, 4)
        page.width = 10
        assert page.area() == 40


class TestTally:
    def test_starts_at_zero(self):
        assert Tally().count == 0

    def test_custom_start(self):
        assert Tally(start=5).count == 5

    def test_click(self):
        clicker = Tally()
        clicker.click()
        clicker.click()
        assert clicker.count == 2

    def test_reset(self):
        clicker = Tally(start=9)
        clicker.reset()
        assert clicker.count == 0

    def test_tallies_are_independent(self):
        first, second = Tally(), Tally()
        first.click()
        assert second.count == 0


class TestPlaylist:
    def test_starts_empty(self):
        playlist = Playlist("Road trip")
        assert playlist.name == "Road trip"
        assert playlist.songs == []

    def test_add_and_count(self):
        playlist = Playlist("Road trip")
        playlist.add("Jolene")
        playlist.add("Hey Jude")
        assert playlist.songs == ["Jolene", "Hey Jude"]
        assert playlist.count() == 2

    def test_playlists_do_not_share_songs(self):
        first, second = Playlist("One"), Playlist("Two")
        first.add("Jolene")
        assert second.songs == []


class TestBankAccount:
    def test_starting_values(self):
        account = BankAccount("Ada")
        assert account.owner == "Ada"
        assert account.balance == 0

    def test_deposit(self):
        account = BankAccount("Ada", 100)
        account.deposit(50)
        assert account.balance == 150

    def test_withdraw(self):
        account = BankAccount("Ada", 100)
        account.withdraw(30)
        assert account.balance == 70

    def test_withdraw_everything(self):
        account = BankAccount("Ada", 100)
        account.withdraw(100)
        assert account.balance == 0

    @pytest.mark.parametrize("amount", [0, -5])
    def test_deposit_must_be_positive(self, amount):
        account = BankAccount("Ada", 100)
        with pytest.raises(ValueError):
            account.deposit(amount)
        assert account.balance == 100

    @pytest.mark.parametrize("amount", [0, -5, 101])
    def test_bad_withdrawals_are_refused(self, amount):
        account = BankAccount("Ada", 100)
        with pytest.raises(ValueError):
            account.withdraw(amount)
        assert account.balance == 100


class TestEmployee:
    @pytest.fixture(autouse=True)
    def reset_headcount(self, monkeypatch):
        monkeypatch.setattr(Employee, "headcount", 0)

    def test_name(self):
        assert Employee("Ada").name == "Ada"

    def test_company_is_shared(self):
        assert Employee("Ada").company == "Acme"
        assert Employee.company == "Acme"

    def test_headcount_goes_up_on_the_class(self):
        Employee("Ada")
        Employee("Bob")
        assert Employee.headcount == 2

    def test_every_instance_sees_the_same_headcount(self):
        ada = Employee("Ada")
        Employee("Bob")
        assert ada.headcount == 2


class TestInventory:
    def test_example(self):
        stock = Inventory()
        stock.add("apple", 5)
        stock.remove("apple", 2)
        assert stock.quantity_of("apple") == 3

    def test_adding_twice_accumulates(self):
        stock = Inventory()
        stock.add("apple", 5)
        stock.add("apple")
        assert stock.quantity_of("apple") == 6

    def test_unknown_item_has_zero(self):
        assert Inventory().quantity_of("pear") == 0

    def test_add_must_be_positive(self):
        with pytest.raises(ValueError):
            Inventory().add("apple", 0)

    def test_remove_unknown_item(self):
        with pytest.raises(KeyError):
            Inventory().remove("pear")

    def test_remove_too_many(self):
        stock = Inventory()
        stock.add("apple", 2)
        with pytest.raises(ValueError):
            stock.remove("apple", 3)
        assert stock.quantity_of("apple") == 2

    def test_item_is_dropped_when_stock_reaches_zero(self):
        stock = Inventory()
        stock.add("apple", 2)
        stock.remove("apple", 2)
        with pytest.raises(KeyError):
            stock.remove("apple")

    def test_low_stock(self):
        stock = Inventory()
        stock.add("pear", 1)
        stock.add("apple", 2)
        stock.add("melon", 10)
        assert stock.low_stock(3) == ["apple", "pear"]
        assert stock.low_stock(1) == []

    def test_total_items(self):
        stock = Inventory()
        assert stock.total_items() == 0
        stock.add("apple", 2)
        stock.add("pear", 3)
        assert stock.total_items() == 5

    def test_inventories_are_independent(self):
        first, second = Inventory(), Inventory()
        first.add("apple")
        assert second.total_items() == 0
