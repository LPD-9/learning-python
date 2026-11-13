from datetime import datetime

import pytest
from orders_report import DATA_FILE, load_orders, main, monthly_total, orders_in_month


def order(order_id, placed_at, total=10.0):
    return {
        "order_id": order_id,
        "placed_at": datetime.fromisoformat(placed_at),
        "total": total,
    }


def ids_in_month(placed_at, year, month):
    return [o["order_id"] for o in orders_in_month([order(1, placed_at)], year, month)]


def test_order_in_the_middle_of_the_month_counts():
    assert ids_in_month("2026-10-15 12:00:00", 2026, 10) == [1]


def test_first_moment_of_the_month_counts():
    assert ids_in_month("2026-10-01 00:00:00", 2026, 10) == [1]


def test_orders_from_the_neighbouring_months_do_not_count():
    assert ids_in_month("2026-09-30 23:59:59", 2026, 10) == []
    assert ids_in_month("2026-11-01 00:00:00", 2026, 10) == []


def test_order_late_on_the_last_day_counts():
    assert ids_in_month("2026-10-31 14:20:00", 2026, 10) == [1]


def test_last_second_of_the_month_counts():
    assert ids_in_month("2026-10-31 23:59:59", 2026, 10) == [1]


def test_a_month_with_thirty_days():
    assert ids_in_month("2026-09-30 18:00:00", 2026, 9) == [1]


def test_a_leap_day():
    assert ids_in_month("2028-02-29 09:00:00", 2028, 2) == [1]


def test_the_end_of_the_year():
    assert ids_in_month("2026-12-31 10:00:00", 2026, 12) == [1]


def test_monthly_total_adds_up_the_orders():
    orders = [order(1, "2026-10-05 10:00:00", 20.0), order(2, "2026-10-20 10:00:00", 5.5)]
    assert monthly_total(orders, 2026, 10) == 25.5


def test_the_data_file_is_loaded():
    assert len(load_orders(DATA_FILE)) == 8


def test_october_total_for_the_data_file():
    assert monthly_total(load_orders(DATA_FILE), 2026, 10) == pytest.approx(510.50)


def test_main_prints_the_october_total(capsys):
    main()
    assert capsys.readouterr().out == "October 2026: 510.50\n"
