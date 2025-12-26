

import sys
import student_mgmt.student as student
from student_mgmt import marks, attendance, fees, report


def main():
    while True:
        print("\n=== STUDENT SYSTEM ===")
        print("1) New Admission (Add Student)")
        print("2) Existing Student (Enter SID)")
        print("3) List All Students")
        print("4) Exit")
        choice = input("Choose: ").strip()

        if choice == '1':
            sid = input("Enter SID (e.g., S101): ").strip()
            name = input("Enter Name: ").strip()
            grade = input("Enter Grade (e.g., 10): ").strip()
            dob = input("Enter DOB (YYYY-MM-DD): ").strip()
            try:
                student.add_student(sid, name, grade, dob)
                print(f"Student '{sid}' added.")
                sub_menu(sid)
            except Exception as e:
                print("Error:", e)

        elif choice == '2':
            sid = input("Enter existing SID: ").strip()
            if student.get_student(sid):
                print(f"Selected student: {sid}")
                sub_menu(sid)
            else:
                print("SID not found.")

        elif choice == '3':
            all_s = student.list_students()
            if not all_s:
                print("No students available.")
            else:
                print("\n--- All Students ---")
                for sid, data in all_s.items():
                    print(f"{sid}: {data.get('name','')} (Grade {data.get('grade','')})")
                print("--------------------")

        elif choice == '4':
            print("Goodbye!")
            sys.exit(0)

        else:
            print("Invalid choice.")

#################




# sub menus
def sub_menu(sid):
    while True:
        print(f"\n=== MENU (SID: {sid}, Name: {student.get_name(sid)}) ===")
        print("1) Edit Student Details")
        print("2) Marks Management")
        print("3) Attendance Management")
        print("4) Fees Management")
        print("5) Report Generation")
        print("6) Back to Start")
        choice = input("Choose: ").strip()

        if choice == '1':
            menu_student(sid)
        elif choice == '2':
            menu_marks(sid)
        elif choice == '3':
            menu_attendance(sid)
        elif choice == '4':
            menu_fees(sid)
        elif choice == '5':
            menu_report(sid)
        elif choice == '6':
            return
        else:
            print("Invalid choice.")











# Sub-menu: Student Management
def menu_student(sid):
    while True:
        print(f"\n--- STUDENT MGMT (SID: {sid}, Name: {student.get_name(sid)}) ---")
        print("1) View student details")
        print("2) Update name")
        print("3) Update grade")
        print("4) Update DOB")
        print("5) Delete student")
        print("6) Back")
        choice = input("Choose: ").strip()

        if choice == '1':
            s = student.get_student(sid)
            if not s:
                print("Student not found.")
            else:
                print(f"SID   : {sid}")
                print(f"Name  : {s.get('name','')}")
                print(f"Grade : {s.get('grade','')}")
                print(f"DOB   : {s.get('dob','')}")

        elif choice == '2':
            name = input("New name: ").strip()
            try:
                student.update_student(sid, name=name)
                print("Updated.")
            except Exception as e:
                print("Error:", e)

        elif choice == '3':
            grade = input("New grade: ").strip()
            try:
                student.update_student(sid, grade=grade)
                print("Updated.")
            except Exception as e:
                print("Error:", e)

        elif choice == '4':
            dob = input("New DOB (YYYY-MM-DD): ").strip()
            try:
                student.update_student(sid, dob=dob)
                print("Updated.")
            except Exception as e:
                print("Error:", e)

        elif choice == '5':
            confirm = input("Delete this student? (y/n): ").strip().lower()
            if confirm == 'y':
                student.delete_student(sid)
                print(f"Deleted '{sid}'.")
                return

        elif choice == '6':
            return

        else:
            print("Invalid choice.")




# Sub-menu: Marks Management
def menu_marks(sid):
    while True:
        print(f"\n--- MARKS MGMT (SID: {sid}) ---")
        print("1) Add/Update subject score")
        print("2) List marks")
        print("3) Show average & grade")
        print("4) Delete a subject")
        print("5) Back")
        choice = input("Choose: ").strip()

        if choice == '1':
            subject = input("Subject: ").strip()
            score = input("Score (0-100): ").strip()
            try:
                marks.add_marks(sid, subject, score)
                print("Saved.")
            except Exception as e:
                print("Error:", e)
        elif choice == '2':
            m = marks.get_marks(sid)
            if not m:
                print("(no marks)")
            else:
                for sub, sc in m.items():
                    print(f"{sub}: {sc}")
        elif choice == '3':
            avg = marks.average(sid)
            grd = marks.grade(avg)
            print(f"Average: {avg:.2f}, Grade: {grd}")
        elif choice == '4':
            subject = input("Subject to delete: ").strip()
            try:
                marks.delete_mark(sid, subject)
                print("Deleted (if existed).")
            except Exception as e:
                print("Error:", e)
        elif choice == '5':
            return
        else:
            print("Invalid choice.")






# Sub-menu: Attendance Management
def menu_attendance(sid):
    while True:
        print(f"\n--- ATTENDANCE MGMT (SID: {sid}) ---")
        print("1) Mark today PRESENT")
        print("2) Mark today ABSENT")
        print("3) Mark specific date (YYYY-MM-DD) present/absent")
        print("4) List records")
        print("5) Show attendance %")
        print("6) Back")
        choice = input("Choose: ").strip()

        if choice == '1':
            attendance.mark_attendance(sid, present=True)
            print("Marked present for today.")
        elif choice == '2':
            attendance.mark_attendance(sid, present=False)
            print("Marked absent for today.")
        elif choice == '3':
            day = input("Date (YYYY-MM-DD): ").strip()
            p = input("Present? (y/n): ").strip().lower()
            present = (p == 'y')
            attendance.mark_attendance(sid, day=day, present=present)
            print("Marked.")
        elif choice == '4':
            recs = attendance.get_attendance(sid)
            if not recs:
                print("(no attendance)")
            else:
                for d, p in recs:
                    print(f"{d}: {'Present' if p else 'Absent'}")
        elif choice == '5':
            pct = attendance.attendance_percentage(sid)
            print(f"Attendance %: {pct:.2f}")
        elif choice == '6':
            return
        else:
            print("Invalid choice.")








# Sub-menu: Fees Management
def menu_fees(sid):
    while True:
        print(f"\n--- FEES MGMT (SID: {sid}) ---")
        print("1) Set fees")
        print("2) Pay fee")
        print("3) Show due, total paid, balance")
        print("4) List payments")
        print("5) Back")
        choice = input("Choose: ").strip()

        if choice == '1':
            amt = input("Fee due amount: ").strip()
            try:
                fees.set_fee(sid, amt)
                print("Fee set.")
            except Exception as e:
                print("Error:", e)

        elif choice == '2':
            amt = input("Payment amount: ").strip()
            try:
                fees.pay_fee(sid, amt)
                print("Payment recorded.")
            except Exception as e:
                print("Error:", e)

        elif choice == '3':
            due = fees.fee_due(sid)
            pays = fees.payments(sid)
            total_paid = sum(a for _, a in pays)
            print(f"Fee Due   : {due:.2f}")
            print(f"Total Paid: {total_paid:.2f}")

        elif choice == '4':
            pays = fees.payments(sid)
            if not pays:
                print("(no payments)")
            else:
                for ts, amt in pays:
                    print(f"{ts} -> {amt:.2f}")


        elif choice == '5':
            return
        else:
            print("Invalid choice.")






# Sub-menu: Report
def menu_report(sid):
    print(f"\n--- REPORT (SID: {sid}) ---")
    print(report.student_report(sid))



main()

