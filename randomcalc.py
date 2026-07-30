import random
import math

luckynumber = random.randint(1,100)
print("Your lucky number is: ", luckynumber)

activities = ["Play a game","Read","Watch movies","Play sports"]
activity = random.choice(activities)
print("Your activity is", activity)

secret_num = random.randint(1,10)

guess = int(input("Enter a number between 1 and 10: "))
if guess == secret_num:
    print("You got it")
else:
    print("Wrong the number was", secret_num)


