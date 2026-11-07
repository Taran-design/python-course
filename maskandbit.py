number = int(input("Enter a number: "))
total_position = int(input("Enter number of positions: "))
for position in range(total_position):
    mask = 1<< position
    print(position)
    print(mask)
    print(bin(mask))
position = int(input("Enter the bit position to check: "))
mark = 1 << position
result = number & mask
if result != 0:
    print("The bit at position", position, "is on")
else:
    print("The bit at position", position,"is off")