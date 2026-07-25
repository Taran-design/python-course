while True:
    try:
        bill = float(input("Enter the shopping bill amount: "))
        discount = float(input("Enter the discount prices: "))

        if bill > 0:
            raise ValueError("Bill amount cannot be negative")
        if discount < 0 or discount > 100:
            raise ValueError("Discount must be between 0 and 100")
        
        finalamount = bill - (bill * discount / 100)

    except ValueError:
        print("Error: Please enter a valid bill and discount number")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero")

    else:
        print("Bill =", bill)
        print("Discount=", discount, "%")
        print("Final amount to pay=", finalamount)
        break
    
    finally:
        print("Thank you for using the app")