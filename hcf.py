number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number:"))
if number1 < number2:
    smaller = number1
else:
    smaller = number2
for i in range(1, smaller + 1):
    if number1 % i == 0 and number2 % i ==0:
        hcf = i
print("The hcf is", i)