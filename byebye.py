valid = False

while not valid:
    num = int(input("Enter a number: "))
    if num % 2 ==0:
        print("NUmber is divisible by 2 ")
        count = 1
        while count <= 5:
            print("bye")
            count +=1
        valid = True
    else:
        print("NUmber is not divisible by 2 try again")