
# report.py — Build a simple text report for a student

from .student import get_student
from .marks import get_marks, average, grade
from .attendance import attendance_percentage
from .fees import  fee_due, payments


def student_report(sid):
    s = get_student(sid)
    if not s:
        return f"Student {sid} not found"

    marks = get_marks(sid)
    avg = average(sid)
    grd = grade(avg)
    attn_pct = attendance_percentage(sid)
    due = fee_due(sid)
    pays = payments(sid)

    lines = []
    lines.append("=" * 50)
    lines.append(f"Student Report - {sid}")
    lines.append("-" * 50)
    lines.append(f"Name   : {s.get('name', '')}")
    lines.append(f"Grade  : {s.get('grade', '')}")
    lines.append(f"DOB    : {s.get('dob', '')}")
    lines.append("")

    # Marks
    lines.append("Marks:")
    if marks:
        for sub, score in marks.items():
            lines.append(f"  {sub}: {score}")
    else:
        lines.append("  (no marks)")
    lines.append(f"Average: {avg:.2f}")
    lines.append(f"Grade  : {grd}")
    lines.append("")

    # Attendance
    lines.append(f"Attendance %: {attn_pct:.2f}")
    lines.append("")

    # Fees
    lines.append(f"Fee Due   : {due:.2f}")
    lines.append("Payments:")
    if pays:
        for ts, amt in pays:
            lines.append(f"  {ts} -> {amt:.2f}")
    else:
        lines.append("  (no payments)")
    lines.append("=" * 50)

    return "\n".join(lines)
