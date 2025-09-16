from grades_analyzer.cli import run

def test_run_table(tmp_path):
    p = tmp_path / "d.csv"
    p.write_text("student_name,subject,teacher_name,date,grade\nA,s,t,2024-01-01,5\nA,s,t,2024-01-02,3\n", encoding="utf-8")
    table = run([str(p)], "students-performance")
    # В таблице должно быть среднее 4.0
    assert "4.0" in table
    assert "student_name" in table and "grade" in table
