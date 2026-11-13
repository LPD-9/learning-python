from log_summary import LOG_FILE, format_summary, main, parse_line, summarise

OLD_STYLE = "2026-10-14 09:15:04 ERROR payments Card declined (code 51)"
NEW_STYLE = "2026-10-14 09:16:11 ERROR [req-8f2a] search Index unavailable"
INFO = "2026-10-14 09:15:01 INFO web Server started"
STACK_TRACE = ['  File "search.py", line 88, in query', "IndexError: shard 3 offline"]


def test_a_log_entry_is_split_into_its_parts():
    assert parse_line(OLD_STYLE) == {
        "time": "2026-10-14 09:15:04",
        "level": "ERROR",
        "component": "payments",
        "message": "Card declined (code 51)",
    }


def test_an_entry_with_a_request_id_is_split_into_its_parts():
    assert parse_line(NEW_STYLE) == {
        "time": "2026-10-14 09:16:11",
        "level": "ERROR",
        "component": "search",
        "message": "Index unavailable",
    }


def test_a_line_that_is_not_an_entry_gives_nothing():
    assert parse_line("Traceback (most recent call last):") is None


def test_a_blank_line_gives_nothing():
    assert parse_line("") is None


def test_summary_counts_levels_and_error_sources():
    summary = summarise([OLD_STYLE, INFO, OLD_STYLE])
    assert summary == {
        "levels": {"ERROR": 2, "INFO": 1},
        "errors_by_component": {"payments": 2},
    }


def test_summary_skips_lines_that_are_not_entries():
    summary = summarise([OLD_STYLE, *STACK_TRACE, ""])
    assert summary == {
        "levels": {"ERROR": 1},
        "errors_by_component": {"payments": 1},
    }


def test_summary_of_the_real_log():
    lines = LOG_FILE.read_text(encoding="utf-8").splitlines()
    assert summarise(lines) == {
        "levels": {"INFO": 5, "ERROR": 3, "WARNING": 1},
        "errors_by_component": {"payments": 2, "search": 1},
    }


def test_summary_layout():
    summary = {
        "levels": {"INFO": 2, "ERROR": 1},
        "errors_by_component": {"payments": 1},
    }
    assert format_summary(summary).splitlines() == [
        "Levels",
        "  ERROR: 1",
        "  INFO: 2",
        "Errors by component",
        "  payments: 1",
    ]


def test_main_prints_the_summary(capsys):
    main()
    assert capsys.readouterr().out.splitlines() == [
        "Levels",
        "  ERROR: 3",
        "  INFO: 5",
        "  WARNING: 1",
        "Errors by component",
        "  payments: 2",
        "  search: 1",
    ]
