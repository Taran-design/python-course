word = input("Enter a word: ")
character = input("Enter a character: ")
count = 0

for letter in word:
    if letter == character:
        count+=1

print(character,"appears",count,"times")