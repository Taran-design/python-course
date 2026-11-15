a = int(input("Enter your first number:"))
b = int(input("Enter your second number:"))
print("First number is", a)
print("Second number is", b)
result = a ^ b 
print("XOR result is", result)
if result < 0:
    print("These numbers have different signs")
else:
    print("These numbers have the same sign")