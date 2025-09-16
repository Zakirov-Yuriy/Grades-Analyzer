from grades_analyzer.models import Record
from grades_analyzer.reports.student_performance import StudentPerformanceReport

def test_student_performance_sort_and_avg():
    rows = [
        Record("A", "s", "t", "2024-01-01", 5),
        Record("B", "s", "t", "2024-01-01", 5),
        Record("A", "s", "t", "2024-01-02", 3),
        Record("B", "s", "t", "2024-01-02", 4),
    ]
    report = StudentPerformanceReport()
    out = report.build(rows)
    assert out == [
        {"student_name": "B", "grade": 4.5},
        {"student_name": "A", "grade": 4.0},
    ]
