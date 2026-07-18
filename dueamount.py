bill = float(input("ENter the bill amount: "))
paid = float(input("Enter the amount paid by the customer: "))

due = bill - paid

if due > 0:
    print("Due amount= ", due)
elif due == 0:
    print("All done")
else:
    print("Change is =", -due)