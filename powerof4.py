n = int(input("Enter a number: "))
if n > 0 and (n & (n - 1)) == 0 and n % 3 == 1:
    print(n, "is a power of 4")
else:
    print(n, "isnt a power of 4")
if n > 0 and (n & (n - 1)) == 0 and n % 7 == 1:
    print(n, "is a power of 8")
else:
    print(n, "isnt a power of 8")