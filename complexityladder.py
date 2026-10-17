guess = input("At n = 1000, 0(n^2) takes how many steps? :")
input("Watch 0(n) and 0(n^2) grow. Press Enter")
for n in [10, 100, 1000]:
    input("n =" + str(n) + "     Press Enter")
    print("  0(n) = ", n, " 0(n^2)= ", n * n)
print(" Your guess:", guess)
input("Full ladder at n = 1000. Press Enter")
print(" 0(1)=1  0(log n)=10  0(n)= 1000  0(n^2)= 1000000")