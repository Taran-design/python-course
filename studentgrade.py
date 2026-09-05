students = {"jack": 83, "bob": 70, "cam": 90, "zach": 60, "josh":75}

total = 0

for score in students.values():
    total += score

average = total / len(students)
print(average)

highest = max(students.values())
lowest = min(students.values())

print(highest)
print(lowest)

for name, score in students.items():
    if score == highest:
        print("Top student is", name)

    if score == lowest:
        print("Bottom student is", name)

name = input("Enter a students name:")
score = students.get(name)

if score:
    print(name, "scored", score)
else:
    print("Student not found")