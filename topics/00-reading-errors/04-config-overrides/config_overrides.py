"""Application config: built-in defaults, overridden by values from an .env file.

An override's name is the setting's name in capitals with an APP_ prefix, so
the `debug` setting is overridden by APP_DEBUG. The type of each default
decides how an override is converted.
"""

from pathlib import Path

ENV_FILE = Path(__file__).parent / "production.env"
DEFAULTS = {"debug": False, "workers": 2, "timeout": 30.0, "name": "api"}


def parse_env_file(text):
    values = {}
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        key, _, value = line.partition("=")
        values[key.strip()] = value.strip().strip("\"'")
    return values


def apply_overrides(defaults, environ, prefix="APP_"):
    config = dict(defaults)
    for key, default in defaults.items():
        raw = environ.get(prefix + key.upper())
        if raw is not None:
            config[key] = type(default)(raw)
    return config


def main():
    environ = parse_env_file(ENV_FILE.read_text(encoding="utf-8"))
    for key, value in apply_overrides(DEFAULTS, environ).items():
        print(f"{key} = {value}")


if __name__ == "__main__":
    main()
