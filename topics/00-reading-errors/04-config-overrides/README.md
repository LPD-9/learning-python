# 04 Config overrides

## Ticket

> **Debug mode is on in production**
>
> Production's config sets `APP_DEBUG=false`, but the service is running in
> debug mode and showing tracebacks to users. The other overrides seem to be
> applied correctly.
>
> Yes/no settings should accept `1`, `true`, `yes` and `on` for yes, and `0`,
> `false`, `no` and `off` for no. Any capitalisation is fine, and spaces
> around the value are ignored. Anything else should be rejected with a
> `ValueError`.

## Run it

```bash
python topics/00-reading-errors/04-config-overrides/config_overrides.py
```

```bash
pytest topics/00-reading-errors/04-config-overrides
```
