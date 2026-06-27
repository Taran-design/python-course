num_rows = int(input("Enter the number of rows: "))

if num_rows % 2 == 0 :
    halfdia = int(num_rows / 2)
else:
    halfdia = int(num_rows / 2)+1

space = halfdia - 1
for i in range(1, halfdia + 1):
    for j in range(1, space + 1):
        print(end = " ")
        space = space - 1
        num = 1

    for j in range(2 * i - 1):
        print(end = str(num))
        num = num + 1
        print()
space = 1
for i in range(1, halfdia):
    for j in range(1, space + 1):
        print(end = " ")
        space = space + 1
        num = 1


    for j in range(1, 2 *(halfdia - i)):
        print(end = str(num))
        print()