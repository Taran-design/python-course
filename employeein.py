class Employee:
    def __init__(self):
        print("Employee created")
    def __del__(self):
        print("Destructer called")

def Create_Obj():
    print("Making object...")
    obj = Employee()
    print("Function ended")
    return obj
print("Calling Create_Obj() function")
obj = Create_Obj()
print("Program ended")
