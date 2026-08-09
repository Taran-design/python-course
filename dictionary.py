students = [

{"id": 101, "name": "Aman", "class": 9, "subject": "Python"},

{"id": 102, "name": "Riya", "class": 9, "subject": "Python"},

{"id": 101, "name": "Aman", "class": 9, "subject": "Python"},

{"id": 103, "name": "Raj", "class": 9, "subject": "Python"},

{"id": 102, "name": "Riya", "class": 9, "subject": "Python"}

]

unique = {}
for student in students:
    student_id = student["id"]
    if student_id not in unique:
        unique[student_id] = student
for student in unique.values():
    print(student)