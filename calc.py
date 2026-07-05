def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def multiply(a,b):
    return a * b

def divide(a, b):
    return a/ b

print("Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter your choice(1-4): "))
num_1 = float(input("Enter a number: "))
num_2 = float(input("Enter another number: "))

if choice == 1:
    print(add(num_1 , num_2))
elif choice == 2:
    print(sub(num_1 , num_2))
elif choice == 3:
    print(multiply(num_1, num_2))
elif choice == 4:
    print(divide(num_1, num_2))
else:
    print("Invalid choice")