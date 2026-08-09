code = {"Codingal" : 2, "is" : 2, "best" : 2, "for" : 2, "Coding" : 1}

frequency = {}

for value in code.values():
    if value in frequency:
        frequency[value] += 1
    else:
        frequency[value] = 1

print(frequency)
