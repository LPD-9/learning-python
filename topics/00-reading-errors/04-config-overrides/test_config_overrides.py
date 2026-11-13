import pytest
from config_overrides import DEFAULTS, ENV_FILE, apply_overrides, main, parse_env_file


def test_comments_and_blank_lines_are_ignored():
    assert parse_env_file("# a comment\n\nAPP_WORKERS=4\n") == {"APP_WORKERS": "4"}


def test_quotes_around_a_value_are_removed():
    assert parse_env_file('APP_NAME="billing api"') == {"APP_NAME": "billing api"}


def test_only_the_first_equals_sign_splits_a_line():
    assert parse_env_file("APP_TOKEN=a=b") == {"APP_TOKEN": "a=b"}


def test_whole_numbers_are_converted():
    config = apply_overrides(DEFAULTS, {"APP_WORKERS": "4"})
    assert config["workers"] == 4
    assert isinstance(config["workers"], int)


def test_decimals_are_converted():
    assert apply_overrides(DEFAULTS, {"APP_TIMEOUT": "2.5"})["timeout"] == 2.5


def test_text_is_kept_as_text():
    assert apply_overrides(DEFAULTS, {"APP_NAME": "billing"})["name"] == "billing"


def test_settings_without_an_override_keep_their_default():
    assert apply_overrides(DEFAULTS, {}) == DEFAULTS


def test_unrelated_variables_are_ignored():
    environ = {"PATH": "/usr/bin", "APP_UNKNOWN": "1"}
    assert apply_overrides(DEFAULTS, environ) == DEFAULTS


def test_the_defaults_are_not_changed():
    before = dict(DEFAULTS)
    apply_overrides(DEFAULTS, {"APP_WORKERS": "9"})
    assert DEFAULTS == before


@pytest.mark.parametrize("text", ["1", "true", "TRUE", "yes", "on", " True "])
def test_values_that_mean_yes(text):
    assert apply_overrides(DEFAULTS, {"APP_DEBUG": text})["debug"] is True


@pytest.mark.parametrize("text", ["0", "false", "False", "no", "off", " OFF "])
def test_values_that_mean_no(text):
    config = apply_overrides({"debug": True}, {"APP_DEBUG": text})
    assert config["debug"] is False


@pytest.mark.parametrize("text", ["maybe", "2", "truee"])
def test_anything_else_is_rejected(text):
    with pytest.raises(ValueError):
        apply_overrides(DEFAULTS, {"APP_DEBUG": text})


def test_the_production_file_is_applied():
    environ = parse_env_file(ENV_FILE.read_text(encoding="utf-8"))
    assert apply_overrides(DEFAULTS, environ) == {
        "debug": False,
        "workers": 4,
        "timeout": 2.5,
        "name": "billing api",
    }


def test_main_prints_the_final_config(capsys):
    main()
    assert capsys.readouterr().out.splitlines() == [
        "debug = False",
        "workers = 4",
        "timeout = 2.5",
        "name = billing api",
    ]
