import pytest
from sales_export import DATA_FILE, format_report, main, read_rows, total_by_region

ROWS = [
    {"date": "2026-10-01", "region": "North", "product": "Widget", "amount": "10.00"},
    {"date": "2026-10-02", "region": "South", "product": "Gadget", "amount": "5.50"},
    {"date": "2026-10-03", "region": "North", "product": "Gadget", "amount": "2.25"},
]
EXPECTED = {"North": 12.25, "South": 5.50}


def sale(amount):
    return {"date": "2026-10-04", "region": "North", "product": "Widget", "amount": amount}


def test_totals_are_added_up_for_each_region():
    assert total_by_region(ROWS) == pytest.approx(EXPECTED)


def test_no_rows_means_no_totals():
    assert total_by_region([]) == {}


def test_unconfirmed_sale_is_not_counted():
    assert total_by_region([*ROWS, sale("")]) == pytest.approx(EXPECTED)


def test_unconfirmed_sale_written_as_spaces_is_not_counted():
    assert total_by_region([*ROWS, sale("   ")]) == pytest.approx(EXPECTED)


def test_report_has_one_line_per_region():
    lines = format_report(EXPECTED).splitlines()
    assert [line.split() for line in lines] == [["North", "12.25"], ["South", "5.50"]]


def test_report_lists_regions_alphabetically():
    lines = format_report({"South": 1.0, "East": 2.0, "North": 3.0}).splitlines()
    assert [line.split()[0] for line in lines] == ["East", "North", "South"]


def test_the_data_file_is_read():
    assert len(read_rows(DATA_FILE)) == 8


def test_totals_for_the_data_file():
    totals = total_by_region(read_rows(DATA_FILE))
    assert totals == pytest.approx({"North": 225.75, "South": 95.75, "East": 299.99})


def test_main_prints_the_report(capsys):
    main()
    words = capsys.readouterr().out.split()
    assert words == ["East", "299.99", "North", "225.75", "South", "95.75"]
