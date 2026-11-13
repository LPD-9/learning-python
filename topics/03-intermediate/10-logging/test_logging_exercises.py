import logging

import pytest
from logging_exercises import (
    divide,
    greet,
    level_for_status,
    load_number,
    log_request,
    make_logger,
    process_orders,
)


@pytest.fixture(autouse=True)
def capture_every_level(caplog):
    caplog.set_level(logging.DEBUG)


def logged(caplog):
    """Return what was logged as (level name, message) pairs."""
    return [(record.levelname, record.getMessage()) for record in caplog.records]


class TestGreet:
    def test_returns_the_greeting(self):
        assert greet("Ada") == "Hello, Ada!"

    def test_logs_at_info(self, caplog):
        greet("Ada")
        assert logged(caplog) == [("INFO", "Greeting Ada")]

    def test_prints_nothing(self, capsys):
        greet("Ada")
        assert capsys.readouterr().out == ""


class TestDivide:
    def test_normal_division_logs_nothing(self, caplog):
        assert divide(10, 4) == 2.5
        assert logged(caplog) == []

    def test_divide_by_zero(self, caplog):
        assert divide(10, 0) is None
        assert logged(caplog) == [("ERROR", "Cannot divide 10 by zero")]


class TestLevelForStatus:
    def test_success_is_info(self):
        assert level_for_status(200) == logging.INFO
        assert level_for_status(302) == logging.INFO
        assert level_for_status(399) == logging.INFO

    def test_client_errors_are_warnings(self):
        assert level_for_status(400) == logging.WARNING
        assert level_for_status(404) == logging.WARNING
        assert level_for_status(499) == logging.WARNING

    def test_server_errors_are_errors(self):
        assert level_for_status(500) == logging.ERROR
        assert level_for_status(503) == logging.ERROR


class TestLogRequest:
    def test_success(self, caplog):
        log_request("GET", "/home", 200)
        assert logged(caplog) == [("INFO", "GET /home -> 200")]

    def test_not_found(self, caplog):
        log_request("GET", "/missing", 404)
        assert logged(caplog) == [("WARNING", "GET /missing -> 404")]

    def test_server_error(self, caplog):
        log_request("POST", "/orders", 500)
        assert logged(caplog) == [("ERROR", "POST /orders -> 500")]

    def test_values_are_passed_as_arguments(self, caplog):
        log_request("GET", "/home", 200)
        assert caplog.records[0].args == ("GET", "/home", 200)


class TestProcessOrders:
    def test_all_valid(self, caplog):
        orders = [{"id": "A1", "quantity": 2}, {"id": "A2", "quantity": 1}]
        assert process_orders(orders) == 2
        assert logged(caplog) == [("INFO", "Processed 2 of 2 orders")]

    def test_bad_orders_are_skipped_with_a_warning(self, caplog):
        orders = [
            {"id": "A1", "quantity": 2},
            {"id": "A2", "quantity": 0},
            {"id": "A3", "quantity": -4},
        ]
        assert process_orders(orders) == 1
        assert logged(caplog) == [
            ("WARNING", "Skipping order A2: bad quantity"),
            ("WARNING", "Skipping order A3: bad quantity"),
            ("INFO", "Processed 1 of 3 orders"),
        ]

    def test_no_orders(self, caplog):
        assert process_orders([]) == 0
        assert logged(caplog) == [("INFO", "Processed 0 of 0 orders")]


class TestLoadNumber:
    def test_valid(self, caplog):
        assert load_number("42") == 42
        assert logged(caplog) == []

    def test_invalid(self, caplog):
        assert load_number("forty-two") is None
        assert logged(caplog) == [("ERROR", "Could not parse forty-two")]

    def test_traceback_is_recorded(self, caplog):
        load_number("forty-two")
        error_type = caplog.records[0].exc_info[0]
        assert error_type is ValueError


class TestMakeLogger:
    @pytest.fixture
    def log_file(self, tmp_path):
        return tmp_path / "app.log"

    @pytest.fixture(autouse=True)
    def close_log_files(self):
        """Close the files afterwards so the temporary folder can be deleted."""
        yield
        for name in ["test_orders", "test_twice", "test_levels"]:
            log = logging.getLogger(name)
            for handler in list(log.handlers):
                handler.close()
                log.removeHandler(handler)

    def read(self, log, log_file):
        for handler in log.handlers:
            handler.flush()
        return log_file.read_text(encoding="utf-8")

    def test_returns_the_named_logger(self, log_file):
        log = make_logger("test_orders", log_file)
        assert log is logging.getLogger("test_orders")

    def test_writes_formatted_messages_to_the_file(self, log_file):
        log = make_logger("test_orders", log_file)
        log.info("started")
        log.warning("low stock")
        expected = "INFO:test_orders:started\nWARNING:test_orders:low stock\n"
        assert self.read(log, log_file) == expected

    def test_debug_messages_are_included(self, log_file):
        log = make_logger("test_levels", log_file)
        log.debug("details")
        assert self.read(log, log_file) == "DEBUG:test_levels:details\n"

    def test_calling_twice_does_not_duplicate_messages(self, log_file):
        make_logger("test_twice", log_file)
        log = make_logger("test_twice", log_file)
        log.info("once")
        assert self.read(log, log_file) == "INFO:test_twice:once\n"
