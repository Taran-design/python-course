height = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))

height = height / 100

bmi = weight/(height*height)
print(bmi)

if bmi >= 18.5:
    print("You are underweight")

if bmi >= 24 : 
    print("You are normal")

if bmi >= 30:
    print("You are overweight")
else:
    print("You are obese")