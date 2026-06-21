lower = int(input("Enter a low range: "))
high = int(input("enter a high range: "))

for num in range(lower, high + 1):
    if num > 1:
        prime = True
        for i in range(2,num):
            if num % i==0:
                prime = False
                break
        if prime:
            print(num)