marks = [75 ,64 ,58, 79, 86, 95, 88 , 69]

print(marks)
print(len(marks))

print("First mark is", marks[0])
print("Last mark is", marks[-1])
print("First three marks are", marks[0:3])

print("All marks are:")
for mark in marks:
    print(marks)

total = sum(marks)
print(total)
average = total / len(marks)
print(average)
smallest = min(marks)
print(smallest)
largest = max(marks)
print(largest)