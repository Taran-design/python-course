n = int(input("Enter the number:"))
j = int(input("Enter the bit position to check:"))
if j < n:
    print("Invalid bit position:")
else:
    bit = (n >> j) & 1
    if bit == 1:
        print("Bit is on")
    else:
        print("Bit is off")
         