num = input("enter a number: ")
middle_digits = num[1:-1]

product = 1
for i in middle_digits:
    product*=int(i)
print(product)