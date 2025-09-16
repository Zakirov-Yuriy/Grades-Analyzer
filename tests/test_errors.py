import pytest
from grades_analyzer import cli
from grades_analyzer.io import read_csv_files
from pathlib import Path
import csv

def test_unknown_report(tmp_path):
    # создаём валидный временный CSV
    p = tmp_path / "ok.csv"
    p.write_text(
        "student_name,subject,teacher_name,date,grade\n"
        "A,s,t,2024-01-01,5\n",
        encoding="utf-8",
    )

    # запускаем cli.run с несуществующим отчётом
    with pytest.raises(SystemExit) as e:
        cli.run([str(p)], "unknown-report")
    assert "Unknown report" in str(e.value)


def test_file_not_found(tmp_path: Path):
    # Проверяем случай, когда файла не существует
    with pytest.raises(SystemExit) as e:
        cli.main(["--files", str(tmp_path / "nofile.csv"), "--report", "students-performance"])
    assert "File not found" in str(e.value)

def test_missing_columns(tmp_path: Path):
    # Проверяем случай, когда в CSV нет нужных колонок
    p = tmp_path / "bad.csv"
    with p.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["wrong_col1", "wrong_col2"])
        writer.writerow(["a", "b"])
    with pytest.raises(ValueError) as e:
        read_csv_files([str(p)])
    assert "missing columns" in str(e.value)

def test_invalid_grade(tmp_path: Path):
    # Проверяем случай, когда grade не число
    p = tmp_path / "badgrade.csv"
    with p.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["student_name","subject","teacher_name","date","grade"])
        writer.writerow(["Иванов Иван","Математика","Петров","2024-01-01","пять"])
    with pytest.raises(ValueError) as e:
        read_csv_files([str(p)])
    assert "Invalid grade" in str(e.value)

    # Ожидаемая логика: пустой список - пустая строка
def test_empty_rows_table():
    from grades_analyzer.tabulate_utils import to_table
    result = to_table([])
    assert result == ""
