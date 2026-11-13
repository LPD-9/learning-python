"""Application settings: built-in defaults, overridden by settings.json.

The service reads its settings when it starts.
"""

import json
from pathlib import Path

SETTINGS_FILE = Path(__file__).parent / "settings.json"
DEFAULTS = {"host": "0.0.0.0", "port": 8000, "debug": False}


class SettingsError(Exception):
    """Raised when the settings can't be loaded."""


def read_settings_file(path):
    try:
        text = path.read_text(encoding="utf-8")
        return json.loads(text)
    except json.JSONDecodeError as error:
        raise SettingsError(f"could not read {path.name}") from error


def load_settings(path=SETTINGS_FILE):
    settings = dict(DEFAULTS)
    settings.update(read_settings_file(path))
    return settings


def main():
    settings = load_settings()
    print(f"Starting on {settings['host']}:{settings['port']}")


if __name__ == "__main__":
    main()
