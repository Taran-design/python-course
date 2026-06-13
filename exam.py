medical_condition = input("Do you have a medical condition: (y/n)")
if medical_condition == "y":
    print("You are eligible for the exam")
else:
    attendance = float(input("What is your attendance? :"))
    if attendance >= 75:
        print("you can take the exam")
    else:
        print("You cant take it ")

