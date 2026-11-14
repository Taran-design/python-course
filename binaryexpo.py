base = int(input("Enter a number: "))
expo = int(input("Enter a power: "))
result = 1
for i in range(expo):
    result = result * base
print("Answer =", result)