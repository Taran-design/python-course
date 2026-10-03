class Account:
    def __init__(self, name, pin):
        self.name = name
        self.pin = pin

    def set_pin(self, new_pin):
        if len(str(new_pin)) == 4:
            self.__pin = new_pin
            print("PIN updated")
        else:
            print("Pin must be 4 digits long")
        
    def __str__(self):
        return f"Account holder: {self.name}, PIN: ****"

account1 = Account("Taran", 1234)
print(account1)
account1.set_pin(4321)

print(account1)