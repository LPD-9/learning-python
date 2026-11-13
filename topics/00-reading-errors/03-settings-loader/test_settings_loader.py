import pytest
from settings_loader import DEFAULTS, SETTINGS_FILE, SettingsError, load_settings, main


def settings_file(tmp_path, text):
    file = tmp_path / "settings.json"
    file.write_text(text, encoding="utf-8")
    return file


def test_defaults_are_used_when_the_file_sets_nothing(tmp_path):
    assert load_settings(settings_file(tmp_path, "{}")) == DEFAULTS


def test_values_in_the_file_override_the_defaults(tmp_path):
    file = settings_file(tmp_path, '{"port": 9000}')
    assert load_settings(file) == {**DEFAULTS, "port": 9000}


def test_settings_that_are_not_defaults_are_kept(tmp_path):
    file = settings_file(tmp_path, '{"region": "eu"}')
    assert load_settings(file) == {**DEFAULTS, "region": "eu"}


def test_invalid_json_is_reported_as_a_settings_error(tmp_path):
    file = settings_file(tmp_path, "{port: 9000}")
    with pytest.raises(SettingsError, match="could not read settings.json"):
        load_settings(file)


def test_the_real_settings_file_is_loaded():
    expected = {"host": "127.0.0.1", "port": 8080, "debug": False}
    assert load_settings(SETTINGS_FILE) == expected


def test_main_says_where_the_service_starts(capsys):
    main()
    assert capsys.readouterr().out == "Starting on 127.0.0.1:8080\n"
