# 03 Settings loader

## Ticket

> **Service won't start after the settings change**
>
> Ops edited `settings.json` to change the host and port, and now the service
> fails on start-up. The error just says it could not read `settings.json`.
> They say the file looks fine and is valid JSON. Please get it starting again.
>
> Settings that aren't valid JSON should still be reported as a
> `SettingsError`.

## Run it

```bash
python topics/00-reading-errors/03-settings-loader/settings_loader.py
```

```bash
pytest topics/00-reading-errors/03-settings-loader
```
