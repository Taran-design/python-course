n = int(input("Enter the number of rounds: "))
total_points = n * n 
print("Total points:", total_points)

total_point_loop = 0
for i in range(n):
    total_point_loop = total_point_loop + n 
print("Total points using loop: ", total_point_loop)

total_point_double = 0
for i in range(n):
    for j in range(n):
        total_point_double = total_point_double + 1
print("Total points using double loop: ", total_point_double)
