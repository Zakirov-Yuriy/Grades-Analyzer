from grades_analyzer.io import read_csv_files
from pathlib import Path
import csv

def test_read_csv_files(tmp_path: Path):
    p = tmp_path / "data.csv"
    with p.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["student_name","subject","teacher_name","date","grade"])
        writer.writerow(["Иванов Иван","Математика","Петров","2024-01-01","4"])
        writer.writerow(["Иванов Иван","Русский","Смирнова","2024-01-02","5"])
    rows = read_csv_files([str(p)])
    assert len(rows) == 2
    assert rows[0].student_name == "Иванов Иван"
    assert rows[0].grade == 4.0
