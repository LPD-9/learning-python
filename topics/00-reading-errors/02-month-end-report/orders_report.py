"""Monthly orders report: how much was ordered in a given month.

Reads orders.csv, which has one row per order: its id, when it was placed,
and its total.
"""

import calendar
import csv
from datetime import datetime
from pathlib import Path

DATA_FILE = Path(__file__).parent / "orders.csv"


def load_orders(path):
    with path.open(newline="", encoding="utf-8") as file:
        return [
            {
                "order_id": int(row["order_id"]),
                "placed_at": datetime.fromisoformat(row["placed_at"]),
                "total": float(row["total"]),
            }
            for row in csv.DictReader(file)
        ]


def month_bounds(year, month):
    start = datetime(year, month, 1)
    last_day = calendar.monthrange(year, month)[1]
    end = datetime(year, month, last_day)
    return start, end


def orders_in_month(orders, year, month):
    start, end = month_bounds(year, month)
    return [order for order in orders if start <= order["placed_at"] <= end]


def monthly_total(orders, year, month):
    return sum(order["total"] for order in orders_in_month(orders, year, month))


def main():
    orders = load_orders(DATA_FILE)
    total = monthly_total(orders, 2026, 10)
    print(f"October 2026: {total:.2f}")


if __name__ == "__main__":
    main()
