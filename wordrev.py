word = input("Enter a word: ")
reverse = ""
for letters in word:
    reverse = letters + reverse

print(reverse)