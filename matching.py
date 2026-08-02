strings = ["123","aba","787","oo","x"]

var = 0

for i in strings:
    if len(i) >= 2 and i[0] == i[-1]:
        var += 1

print(var)