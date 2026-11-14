n = int(input("Enter a number: "))
if n > 0 and (n & (n - 1)) == 0:
    print(n ,"is a power of 2")
else:
    print(n, "isnt a power of 2")