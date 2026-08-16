students = {"john": "math", "sarah": "science", "mike": "english", "john": "math"}

students["Alex"] = "history"
students["sarah"] = "math"

del students["mike"]

print("number of students:", len(students))

for name, subject in students.items():
    print(name,":", subject)