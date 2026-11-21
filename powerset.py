numbers = [10, 20, 30]
n = len(numbers)
total_subsets = 1 << n 
print("Total Subsets =", total_subsets)
for mask in range(n):
    subset = []
    for j in range(n):
        if (mask >> j) & 1:
            subset.append(numbers[j])
        print("Mask:", mask,"Subset:", subset)