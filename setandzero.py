number = int(input("Enter a number: "))
position = int(input("Enter a bit position to SET: "))
mask = 1 << position
setresult = number | mask
print(bin(setresult))
position = int(input("Enter a bit position to CLEAR: "))
mark = -(1 << mask)
clearresult = number & mask 
print(clearresult)
if number > 0 and (number & (number - 1)) == 0:
    print("The number is a power of 2")
else:
    print("The number is not a power of 2")