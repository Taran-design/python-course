number = int(input("Emter a positive number: "))
if number <= 0:
    print("Please enter a positive number")
else:
    print("Factors of", number,"are:")
    i = 1
    while i <= number:
        if number % i == 0:
            print(i)
        i += 1