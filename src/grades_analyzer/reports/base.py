from __future__ import annotations
from typing import Protocol, Sequence, List, Any

class Report(Protocol):
    name: str

    def build(self, rows: Sequence[Any]) -> List[dict]:
        """Построит табличные данные для отчёта.
        Возвращает список словарей (строк), готовых для табличного вывода.
        """

