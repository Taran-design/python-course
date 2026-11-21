a = int(input("Enter number A:"))
b = int(input("Enter number B:"))
xor_result = a ^ b
print("XOR result:", xor_result)
count = 0
while xor_result > 0:
    if xor_result & 1:
        count += 1
    xor_result = xor_result >> 1
print("Number of different bits:", count)