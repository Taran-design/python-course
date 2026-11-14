def binary_to_decimal(binary):
    decimal = 0
    power = 0

    while binary > 0:
        digit = binary % 10
        decimal += digit * (2 ** power)
        binary //= 10
        power += 1

    return decimal


def decimal_to_binary(decimal):
    binary = ""

    if decimal == 0:
        return "0"

    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal //= 2

    return binary


print("Binary and Decimal Converter")
print("1. Binary to Decimal")
print("2. Decimal to Binary")

choice = input("Choose an option: ")

if choice == "1":
    number = int(input("Enter a binary number: "))
    print("Decimal:", binary_to_decimal(number))

elif choice == "2":
    number = int(input("Enter a decimal number: "))
    print("Binary:", decimal_to_binary(number))

else:
    print("Invalid choice")