num = int(input("Enter a number: "))
original = num
result = 0
while num > 0:
    digit = num % 10
    result = result + (digit ** 3)
    num = num // 10

if original == result:
    print("it is an armstrong number")
else:
    print("It is not an armstrong number")