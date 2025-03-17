students_marks = {
    'Alice': 85,
    'Bob': 92,
    'Charlie': 78,
    'David': 88,
    'Eve': 95
}
student_name = input("Enter the student's name: ")
if student_name in students_marks:
    print(f"{student_name}'s marks are: {students_marks[student_name]}")
else:
    print(f"Student '{student_name}' not found in the records.")