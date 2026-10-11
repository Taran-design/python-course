n = int(input("Enter the input size of n: "))
if n < 1:
    print("Please enter a positive integer")
else:
    single_count = 0
    for i in range(n):
        single_count += 1
    nested_count = 0
    for i in range(n):
        for j in range(n):
            nested_count += 1
    print("\nLoop comparison:")
    print("Input size:", n)
    print("Single loop steps:", single_count)
    print("Nested loop steps:", nested_count)
    print("\nComplexity:")
    print("Single loop: 0(n), 0(n), 0(n)")
    print("Nested loops: 0(n^2), 0(n^2), 0(n^2)")
    print("\nThe single loop forws linearly")
    print("The nested loops grow quadratically")