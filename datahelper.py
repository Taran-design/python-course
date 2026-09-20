class DataHelper:
    def __init__(self, data=[10, 20, 30, 40, 50]):
        self.data = data
        print("Data helper has been created")

    def show_data(self):
        for index, value in enumerate(self.data):
            print(index, value)
    
    def __del__(self):
        print("Data helper has been destroyed")

helper = DataHelper()
helper.show_data()
del helper