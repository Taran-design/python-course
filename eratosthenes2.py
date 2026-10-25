def sieve(num):
    prime = [True for i in range(num + 1)]
    p = 2
    while p * p <= num:
        if prime[p]:
            for i in range(p * p, num + 1, p):
                prime[i] = False
        
        p += 1
    prime[0] = False
    if num >= 1:
        prime[1] = False
    for p in range(2, num + 1):
        if prime[p]:
            print(p, end = " ")
    print()
highestnumber = int(3000)
sieve(highestnumber)