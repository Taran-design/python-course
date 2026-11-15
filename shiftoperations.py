num = int(input("Enter a number:"))
print("Original number:", num)
print("Binary representation:", bin(num))
left_one = num << 1
left_two = num << 2
right_one = num >> 1
right_two = num >> 2
print("Left shift by 1:", left_one)
print("Left shift by 2:", left_two)
print("Right shift by 1:", right_one)
print("Right shift by 2:", right_two)