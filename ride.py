print("1. bike")
print("2. car")
ride = int(input("Which ride do you want: "))
if ride == 1:
    print("1. Scooter")
    print("2. sports bike")
    bike = int(input("Which bike do you want: "))
    if bike == 1:
        print("You selected a scooter")
    else:
        print("You selected sports bike")
else:
    print("1. Sudan")
    print("2. SUV")
    car = int(input("Which car would you like: "))
    if car == 1:
        print("You chose the sudan")
    else:
        print("You chose the SUV")