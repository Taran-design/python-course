units = int(input("How many units have you used? :"))
if units < 50:
    cost = units * 2.6 
    tax = 25
else:
    if units < 100:
        cost = units * 3.25
        tax = 35
    else:
        if units < 200:
            cost = units * 5.26
            tax = 45
        else:
            cost = units * 8.45
            tax = 75
    
bill = cost + tax 
print(bill)