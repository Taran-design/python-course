number = int(input("Enter a number: "))
position = 0
if number == 0:
    print("No set bit found")
else:
    while (number & 1) == 0:
        number = number >> 1
        position += 1
        print("Position of the rightmost set bit:", position)