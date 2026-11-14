secretcode = int(input("Enter a secret code in binary:"))
access = int(input("Enter the access key in binary: "))

mask = 255

print("Secret code:", bin(secretcode))
print("And:", secretcode & access)

print("OR:", secretcode | access)
print("XOR:", secretcode ^ access)
print("Left shift:", secretcode << 1)
print("Right shift:", secretcode >> 1)
def countbits(secretcode):
    count = 0
    while secretcode > 0:
        secretcode = secretcode & (secretcode - 1)
        count += 1
    return count
print("Count bits secret code", countbits(secretcode))