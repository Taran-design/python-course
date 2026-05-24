money = int(input("How much money do you have?: "))
note100 = money//100
money = money % 100
note50 =money // 50
money = money % 50
note10 = money // 10
money = money % 10
print(note100)
print(note50)
print(note10)