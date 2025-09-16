from __future__ import annotations
from typing import Iterable, List
import csv
from .models import Record

REQUIRED_COLUMNS = ("student_name", "subject", "teacher_name", "date", "grade")

def read_csv_files(paths: Iterable[str]) -> List[Record]:
    records: List[Record] = []
    seen_any = False
    for path in paths:
        seen_any = True
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            # Валидация заголовков
            missing = [c for c in REQUIRED_COLUMNS if c not in reader.fieldnames]  # type: ignore[arg-type]
            if missing:
                raise ValueError(f"CSV {path} missing columns: {', '.join(missing)}")
            for row in reader:
                try:
                    grade = float(row["grade"])
                except (TypeError, ValueError):
                    # Считаем содержимое валидным по условию задачи, но на всякий случай
                    raise ValueError(f"Invalid grade in {path}: {row.get('grade')}")
                records.append(
                    Record(
                        student_name=(row["student_name"] or "").strip(),
                        subject=(row["subject"] or "").strip(),
                        teacher_name=(row["teacher_name"] or "").strip(),
                        date=(row["date"] or "").strip(),
                        grade=grade,
                    )
                )
    if not seen_any:
        raise ValueError("No CSV files provided")
    return records
