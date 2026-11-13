# 05 Log summary

## Ticket

> **Daily log summary crashes**
>
> Since Tuesday's logging upgrade, the daily log summary crashes instead of
> printing. Operations still want the same summary as before.
>
> Lines in the log that aren't log entries, such as stack traces, shouldn't
> appear in the summary and shouldn't stop it from running.

## Run it

```bash
python topics/00-reading-errors/05-log-summary/log_summary.py
```

```bash
pytest topics/00-reading-errors/05-log-summary
```
