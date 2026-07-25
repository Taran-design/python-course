import random 

choices = ["rock","paper","scissors"]

computer = random.choice(choices)

user_input = input("Choose rock paper or scissors: ")
print("The computer chose:", computer)

if user_input == computer:
    print("Its a match")
else:
    print("Its not a match")

