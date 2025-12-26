
MARKS = {}


def add_marks(sid, subject, score):

    if sid is None or str(sid).strip() == "":
        raise ValueError("Student ID cannot be empty")
    if subject is None or str(subject).strip() == "":
        raise ValueError("Subject cannot be empty")

    # basic validation
    try:
        score = float(score)
    except Exception:
        raise ValueError("Score must be a number")

    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")

    MARKS.setdefault(sid, {})
    MARKS[sid][subject.strip()] = score


def get_marks(sid):
    """
    Return subject-score dictionary for a student.
    If no marks present, returns empty dict.
    """
    return MARKS.get(sid, {}).copy()


def update_mark(sid, subject, score):
    if sid not in MARKS or subject not in MARKS[sid]:
        raise KeyError("Marks for this subject do not exist")
    add_marks(sid, subject, score)  # reuse validation


def delete_mark(sid, subject):

    if sid in MARKS and subject in MARKS[sid]:
        del MARKS[sid][subject]
        if not MARKS[sid]:
            del MARKS[sid]


def average(sid):
    subjects = MARKS.get(sid, {})
    if not subjects:
        return 0.0
    total = sum(subjects.values())
    return total / len(subjects)


def grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 75:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 40:
        return "C"
    else:
        return "D"
