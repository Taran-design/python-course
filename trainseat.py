def iterative_binary_search(seats, target):
    left = 0
    right = len(seats) - 1

    while left <= right:
        mid = (left + right) // 2

        if seats[mid] == target:
            return mid
        elif seats[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        
    return -1

def recursive_binary_search(seats, target, left, right):
    if left > right:
        return -1
    
    mid = (left + right) // 2
    if seats[mid] == target:
        return mid
    elif seats[mid] < target:
        return recursive_binary_search(seats, target, mid + 1, right)
    else:
        return recursive_binary_search(seats, target, left, mid - 1)

seats = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

target = int(input("Enter the train seat number to find: "))
result1 = iterative_binary_search(seats, target)

if result1 != -1:
    print("Iterative search: Seat found at position", result1)
else:
    print("Iterative search: Seat not found")

result2 = recursive_binary_search(seats, target, 0, len(seats) - 1)

if result2 != -1:
    print("Recursive search: Seat found at position", result2)
else:
    print("Recursive search: Seat not found")

print("\nComplexity comparison:")
print("Iterative binary search")
print("Time complexity: 0(log n)")
print("Space complexity: 0(1)")
print("Call stack usage: 0(1)")

print("Recursive binary search:")
print("Time complexity: 0(log n)")
print("Space complexity: 0(log n)")
print("Call stack usage: 0(log n)")