import random 

random_number = random.randint(1, 10)

num = int(input("Enter a number between 1 and 10: "))

if num == random_number:
    print("You guessed the right number")
else:
    print("Wrong guess")
    print("The number was", random_number)