def cube(number):
    return number ** 3

def div(number):
    if number % 3 == 0:
        print(cube(number))
    else:
        print("The number is not divisible by 3")

div(6)