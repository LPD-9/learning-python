# 01 Sales export

## Ticket

> **Monthly sales export is crashing**
>
> The monthly sales export worked fine last month. Since this month's
> `sales.csv` arrived it crashes instead of printing the report, and Finance
> need the numbers today.
>
> Finance say some of the sales in the file are still waiting to be
> confirmed. Those shouldn't count towards the totals.

## Run it

```bash
python topics/00-reading-errors/01-sales-export/sales_export.py
```

```bash
pytest topics/00-reading-errors/01-sales-export
```
