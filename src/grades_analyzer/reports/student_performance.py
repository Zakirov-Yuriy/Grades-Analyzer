from __future__ import annotations
from typing import Sequence, Dict, List
from collections import defaultdict
from ..models import Record
from .base import Report

class StudentPerformanceReport(Report):
    name = "students-performance"

    def build(self, rows: Sequence[Record]) -> List[dict]:
        # Считаем средний балл по студенту
        sums: Dict[str, float] = defaultdict(float)
        counts: Dict[str, int] = defaultdict(int)
        for r in rows:
            sums[r.student_name] += r.grade
            counts[r.student_name] += 1
        result = [
            {
                "student_name": name,
                "grade": round(sums[name] / counts[name], 1),
            }
            for name in sums
        ]
        # Сортировка по убыванию среднего, затем по имени
        result.sort(key=lambda x: (-x["grade"], x["student_name"]))
        return result
