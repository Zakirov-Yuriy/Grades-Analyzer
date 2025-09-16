from __future__ import annotations
import argparse
from typing import Dict, List, Type
from .io import read_csv_files
from .tabulate_utils import to_table
from .models import Record
from .reports.base import Report
from .reports.student_performance import StudentPerformanceReport

REPORTS_REGISTRY: Dict[str, Report] = {
    StudentPerformanceReport.name: StudentPerformanceReport(),
}

def parse_args(argv: List[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Анализ успеваемости студентов")
    parser.add_argument(
        "--files",
        nargs="+",
        metavar="CSV",
        help="пути к CSV-файлам",
        required=True,
    )
    parser.add_argument(
        "--report",
        choices=list(REPORTS_REGISTRY.keys()),
        help="название отчёта",
        required=True,
    )
    return parser.parse_args(argv)

def run(files: List[str], report_name: str) -> str:
    records: List[Record] = read_csv_files(files)
    report = REPORTS_REGISTRY.get(report_name)
    if not report:
        raise SystemExit(f"Unknown report: {report_name}")
    rows = report.build(records)
    table = to_table(rows)
    return table

def main(argv: List[str] | None = None) -> None:
    args = parse_args(argv)
    try:
        output = run(args.files, args.report)
        print(output)
    except FileNotFoundError as e:
        raise SystemExit(f"File not found: {e.filename}") from e
    except ValueError as e:
        raise SystemExit(str(e)) from e

if __name__ == "__main__":
    main()
