for num in range(1, 21):
    if num % 20 == 0:
        print("Twist")
    elif num % 15 == 0:
        pass
    elif num % 5 == 0:
        print("Fizz")
    elif num % 3 == 0:
        print("Buzz")
    else:
        print(num)