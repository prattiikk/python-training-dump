'''
Case Study 1: Student Grade Calculator
Write a program to store marks of 5 students in a dictionary. Each student should have 3 subjects.
Create a function to calculate the average marks of each student.
Based on the average, assign grades using control statements:
A: 90 and above
B: 75–89
C: 60–74
Fail: below 60
Print the student name, average marks, and grade.
Modify the program to display the top scorer’s name and average marks.

'''


def calc_average(marks):
    return (marks[0] + marks[1] + marks[2]) / 3

def print_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75 and avg <= 89:
        return "B"
    elif avg >= 60 and avg <= 74:
        return "C"
    else:
        return "Fail"


def top_scorer(averages):
    top_name = None
    top_avg = 0
    for name in averages:
        if averages[name] > top_avg:
            top_avg = averages[name]
            top_name = name
    print(top_name, "with Avg:", top_avg)

def main():
    students_marks = {
        "Aman":  [92, 88, 95],
        "Bhakti":[74, 68, 70],
        "Chetan":[81, 79, 84],
        "Divya": [59, 62, 55],
        "Esha":  [90, 93, 89]
    }


# this creates another dict where name is key and average is its value
    averages = {}
    for name in students_marks:
        avg = calc_average(students_marks[name])
        averages[name] = round(avg, 2)


    names = list(students_marks.keys())
    names.sort()

    for name in names:
        avg = averages[name]
        print(f"Name : {name}")
        print(f"Average Marks : {avg}")
        print(f"Grade : ", print_grade(avg))
        print("------"*3)

    print("Top scorer:")
    top_scorer(averages)

main()
