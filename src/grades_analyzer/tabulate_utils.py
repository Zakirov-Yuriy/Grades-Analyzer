from __future__ import annotations
from typing import List, Dict
from tabulate import tabulate

def to_table(rows: List[Dict], headers: Dict[str, str] | None = None) -> str:
    if headers is None and rows:
        headers = {k: k for k in rows[0].keys()}
    headers = headers or {}
    table = tabulate(
        [list(r.values()) for r in rows],
        headers=list(headers.values()),
        tablefmt="grid",
        floatfmt=".1f",
        colalign=("left", "right") if rows else None,
        showindex=range(1, len(rows) + 1) if rows else False,
    )
    return table
