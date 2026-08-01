def add(a,b):
    return a + b 

def subtract(a, b):
    return a - b 

def multiply(a , b):
    return a * b

def divide(a , b):
    return a / b

while True:
    print("Choose an operation: ")
    print(1. Add)
    print(2. Subtract)
    print(3. Multiply)
    print(4. Divide)
    
    choice = input("Enter your choice:")
    if choice > 4:
        print("Calculator stopped")
        break
    
    try:
        num1 = float(input("Enter a number:"))
        num2 = float(input("Enter another number: "))

        if choice == 1:
            print(add(num1, num2))
        elif choice == 2:
            print(subtract(num1,num2))
        elif choice ==3:
            print(multiply(num1,num2))
        elif choice == 4:
            print(divide(num1,num2))
        else:
            print("Invalid operation")
    
    except ValueError:
        print("Error : Enter numbers only")
    
    except ZeroDivisionError:
        print("Error : Cannot divide by zero")