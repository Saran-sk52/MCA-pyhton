student = {
    "name": "John Doe",
    "r.no": "12345",
    "reg.no.": "98765",
    "dep.": "Computer Science",
    "sem.": 5,
    "total_marks": 85
}
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
del student['r.no']
print(student)
