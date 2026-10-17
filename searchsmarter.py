numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
target = 70
left = 0
right = len(numbers) - 1
check = 0
found_index = -1
while left <= right:
    mid = (left + right) // 2
    print("Checking index:",mid ,"Value:",numbers[mid])
    if numbers[mid] == target:
        found_index = mid
        break
    elif numbers[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
if found_index != 1:
    print("Target found:", target)
    print("Index:", found_index)
else:
    print("Target not found")
print("Total check:", check)