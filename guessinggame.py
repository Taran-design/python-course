import random 
secret_num = random.randint(1, 50)
lives = 5 

print("You have to guess the number im thinking of that is between 1 and 50.")
print("You have 5 lives")

while lives > 0 :
    guess = int(input("Enter a number: "))

    if guess == secret_num:
        print("You found the secret number")
        break
    else:
        difference = abs(secret_num - guess)

        if difference <= 5:
            print("You are very close")
        elif difference <= 10:
            print("You are close")
        else:
            print("Try again")

        lives -= 1

        print("Lives remaining =", end=" ")
        for i in range(lives):
            print("£", end=" ")
        print("You have",lives ,"left")

if lives == 0:
    print("You didnt guess it")
    print("The number was", secret_num)