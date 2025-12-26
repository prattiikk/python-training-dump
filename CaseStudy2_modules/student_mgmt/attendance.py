
ATTENDANCE = {}


def mark_attendance(sid, day=None, present=True):
    if not sid or str(sid).strip() == "":
        raise ValueError("Student ID cannot be empty")

    if day is None:
        import time
        day = time.strftime("%Y-%m-%d")

    ATTENDANCE.setdefault(sid, [])
    ATTENDANCE[sid].append((day, bool(present)))


def get_attendance(sid):
    return ATTENDANCE.get(sid, []).copy()


def attendance_percentage(sid):
    records = ATTENDANCE.get(sid, [])
    if not records:
        return 0.0
    total = len(records)
    present_days = sum(1 for _, p in records if p)
    return (present_days / total) * 100.0

