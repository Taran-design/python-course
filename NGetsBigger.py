sizes = [4, 10 , 100 , 1000]
for n in sizes:
    steps = 0
    for i in range(n):
        for j in range(n):
            steps = steps + 1
    print("n =", n ,"! Steps =", steps)
