from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class Record:
    student_name: str
    subject: str
    teacher_name: str
    date: str
    grade: float
