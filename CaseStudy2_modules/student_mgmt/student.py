
STUDENTS = {}


import random

def generate_sid(prefix="S", width=3):
    number = random.randint(1, 10**width - 1)
    return f"{prefix}{number:0{width}d}"




def add_student(sid, name, grade, dob):
    if not sid or sid.strip() == "":
        raise ValueError("Student ID cannot be empty")
    if sid in STUDENTS:
        raise ValueError(f"Student '{sid}' already exists")
    if not name.strip():
        raise ValueError("Name cannot be empty")

    STUDENTS[sid] = {
        "name": name.strip(),
        "grade": str(grade).strip(),
        "dob": dob,
    }

def get_name(sid):
    return STUDENTS[sid]["name"]

def get_student(sid):
    return STUDENTS.get(sid)

def list_students():
    return STUDENTS

def update_student(sid, name=None, grade=None, dob=None):
    if sid not in STUDENTS:
        raise KeyError(f"Student '{sid}' not found")
    s = STUDENTS[sid]

    if name is not None:
        if not name.strip():
            raise ValueError("Name cannot be empty")
        s["name"] = name.strip()

    if grade is not None:
        s["grade"] = str(grade).strip()

    if dob is not None:
        s["dob"] = dob


def delete_student(sid):
    STUDENTS.pop(sid, None)
