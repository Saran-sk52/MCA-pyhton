student = {
    "name": input("Enter student name: "),
    "roll.no": input("Enter roll number of the student: "),
    "reg.no.": input( "Enter register number: "),
    "department.": input("Enter department name: "),
    "sem.": input("Enter the semester:"),
}
print(student)
student.update({"total_marks":int(input("Enter total marks: "))})
print("After adding total marks and grade:")
def calculate_grade(total_marks):
    if total_marks >= 90:
        return 'A'
    elif total_marks >= 82:
        return 'B'
    elif total_marks >= 75:
        return 'C'
    elif total_marks >= 60:
        return 'D'
    elif total_marks >= 50:
        return 'P'
    else:
        return 'F'
student['grade'] = calculate_grade(student['total_marks'])
print(student)
print("After deleting roll number:")
del student['roll.no']
print(student)
