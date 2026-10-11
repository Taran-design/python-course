n = int(input("Enter the input size of n: "))
if n < 1:
    print("Please enter a positive integer")
else:
    constant_steps = 1
    linear_steps = 0
    for i in range(n):
        linear_steps += 1
    quadratic_steps = 0
    for i in range(n):
        quadratic_steps += 1
    print("\nOperation counts:")
    print("Costant algorithm:", constant_steps)
    print("Single loop:", linear_steps)
    print("Double loop:", quadratic_steps)
    print("\nComplexity classifications: ")
    print("Constant algorithm: 0(1), 0(1), 0(1)")
    print("Single loop: 0(n), 0(n), 0(n)")
    print("Double loop: 0(n^2), 0(n^2), 0(n^2)")
