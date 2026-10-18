number = int(input("Enter a number: "))
og_number = number
number_of_digits = len(str(number))
sum_of_powers = 0
temp = number
while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** number_of_digits
    temp = temp //10
if sum_of_powers == og_number:
    print(og_number, "is an armstrong number")
else:
    print(og_number, "is not an armstrong number")