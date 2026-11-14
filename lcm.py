num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

lcm = max(num1, num2)

while True:
    if lcm % num1 == 0 and lcm % num2 == 0:
        break
    lcm += 1

print("The LCM is:", lcm)