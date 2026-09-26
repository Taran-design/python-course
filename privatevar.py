class myClass:
    __privateVar = 27;
    def __privMeth(self):
        print("Im inside class myClass")
    def hello(self):
        print("Private variable value: ",myClass.__privateVar)
foo = myClass()
foo.hello()
foo._myClass__privMeth()