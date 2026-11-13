import json
import math

import pytest
from inheritance_exercises import (
    Animal,
    CardPayment,
    CashPayment,
    Cat,
    Circle,
    Dog,
    EmailNotifier,
    Employee,
    JsonMixin,
    Manager,
    MultiNotifier,
    Notifier,
    PaymentMethod,
    Product,
    Shape,
    SmsNotifier,
    Square,
    total_area,
)


class TestAnimals:
    def test_dog(self):
        assert Dog("Rex").describe() == "Rex says Woof"

    def test_cat(self):
        assert Cat("Tom").describe() == "Tom says Meow"

    def test_they_are_animals(self):
        assert isinstance(Dog("Rex"), Animal)
        assert isinstance(Cat("Tom"), Animal)

    def test_describe_is_inherited_not_rewritten(self):
        assert "describe" not in vars(Dog)
        assert "describe" not in vars(Cat)


class TestManagerInit:
    def test_attributes(self):
        manager = Manager("Grace", 90000, ["Ada", "Bob"])
        assert manager.name == "Grace"
        assert manager.salary == 90000
        assert manager.reports == ["Ada", "Bob"]

    def test_is_an_employee(self):
        assert isinstance(Manager("Grace", 90000, []), Employee)


class TestManagerDescribe:
    def test_example(self):
        manager = Manager("Grace", 90000, ["Ada", "Bob"])
        assert manager.describe() == "Grace (£90000), manages 2 people"

    def test_no_reports(self):
        assert Manager("Grace", 1, []).describe() == "Grace (£1), manages 0 people"

    def test_uses_the_parent_description(self, monkeypatch):
        monkeypatch.setattr(Employee, "describe", lambda self: "PARENT")
        assert Manager("Grace", 1, ["Ada"]).describe() == "PARENT, manages 1 people"


class TestShapes:
    def test_square(self):
        assert Square(3).area() == 9

    def test_circle(self):
        assert Circle(2).area() == pytest.approx(math.pi * 4)

    def test_they_are_shapes(self):
        assert isinstance(Square(1), Shape)
        assert isinstance(Circle(1), Shape)

    def test_total_area(self):
        assert total_area([Square(2), Square(3)]) == 13
        assert total_area([Square(1), Circle(1)]) == pytest.approx(1 + math.pi)

    def test_total_area_of_nothing(self):
        assert total_area([]) == 0

    def test_total_area_works_with_shapes_it_has_never_seen(self):
        class Triangle(Shape):
            def area(self):
                return 6

        assert total_area([Triangle(), Square(2)]) == 10


class TestPaymentMethods:
    def test_card(self):
        assert CardPayment("1234").pay(12.5) == "Paid £12.50 with card ending 1234"

    def test_cash(self):
        assert CashPayment().pay(3) == "Paid £3.00 in cash"

    def test_template_cannot_be_created(self):
        with pytest.raises(TypeError):
            PaymentMethod()

    def test_subclass_without_pay_cannot_be_created(self):
        class Forgetful(PaymentMethod):
            pass

        with pytest.raises(TypeError):
            Forgetful()

    def test_they_are_payment_methods(self):
        assert isinstance(CardPayment("1234"), PaymentMethod)
        assert isinstance(CashPayment(), PaymentMethod)


class TestJsonMixin:
    def test_product(self):
        assert json.loads(Product("pen", 2.5).to_json()) == {
            "name": "pen",
            "price": 2.5,
        }

    def test_keys_are_sorted(self):
        assert Product("pen", 2.5).to_json() == '{"name": "pen", "price": 2.5}'

    def test_works_for_any_class(self):
        class Pet(JsonMixin):
            def __init__(self):
                self.species = "cat"
                self.age = 3

        assert Pet().to_json() == '{"age": 3, "species": "cat"}'

    def test_to_json_lives_on_the_mixin(self):
        assert "to_json" not in vars(Product)


class TestNotifiers:
    def test_email(self):
        notifier = EmailNotifier("ada@example.com")
        assert notifier.send("Hi") == ["Email to ada@example.com: Hi"]

    def test_sms(self):
        assert SmsNotifier("07700 900123").send("Hi") == ["SMS to 07700 900123: Hi"]

    def test_sms_is_cut_to_twenty_characters(self):
        message = "Your parcel will arrive between 9 and 11"
        sent = SmsNotifier("0123").send(message)
        assert sent == ["SMS to 0123: Your parcel will arr"]

    def test_multi_sends_through_each(self):
        multi = MultiNotifier([EmailNotifier("a@b.com"), SmsNotifier("0123")])
        assert multi.send("Hi") == ["Email to a@b.com: Hi", "SMS to 0123: Hi"]

    def test_multi_with_nothing_inside(self):
        assert MultiNotifier([]).send("Hi") == []

    def test_they_are_all_notifiers(self):
        for notifier in [EmailNotifier("a@b.com"), SmsNotifier("1"), MultiNotifier([])]:
            assert isinstance(notifier, Notifier)

    def test_multi_can_be_nested(self):
        inner = MultiNotifier([SmsNotifier("1"), SmsNotifier("2")])
        outer = MultiNotifier([EmailNotifier("a@b.com"), inner])
        assert outer.send("Hi") == [
            "Email to a@b.com: Hi",
            "SMS to 1: Hi",
            "SMS to 2: Hi",
        ]
