numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
target = int(input("Enter the number to search for: "))
checks = 0
found = False
for number in numbers:
    checks += 1
    if number == target:
        found = True
        break
if found:
    print("Number found:", target)
else:
    print("Number not found:", target)
print("Comparisons performed:", checks)
best_case = 1
worst_case = len(numbers)
average_case = (len(numbers) + 1) / 2
print("\nLinear search comparisons counts:")
print("Best case:", best_case)
print("Average successful case:", average_case)
print("Worst case:", worst_case)
print("\nTime complexity: ")
print("Best case: 0(1)")
print("Average successful case: 0(n)")
print("Worst case: 0(n)")