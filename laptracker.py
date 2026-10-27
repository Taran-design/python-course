laps = int(input("Enter a number of laps: "))
total = laps * (laps + 1) // 2
print("Formula: ",total)

total = 0
for i in range(1, laps + 1):
    total += i 

print("Loop:", total)
total = 0

for i in range(1, laps + 1):
    for j in range(i):
        total += 1

print("Nested loop:", total)