numbers = [2, 4, 7, 2, 4, 9]
xor_result = 0
for num in numbers:
    xor_result = xor_result ^ num
rightmost_set_bit = xor_result & ~xor_result
num1 = 0
num2 = 0
for num in numbers:
    if (num & rightmost_set_bit) != 0:
        num1 = num1 ^ num
    else:
        num2 = num2 ^ num
print("First odd occuring number:", num1)
print("Second odd occuring number:", num2)