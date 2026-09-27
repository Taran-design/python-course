class India():
    def capital(self):
        print("New dehli is the capital of india")
    def language(self):
        print("Hindi is the most spoken language in india")
    def type(self):
        print("India is a developing country")
class USA():
    def capital(self):
        print("The capital is washington D.C.")
    def language(self):
        print("The most spoken language is english")
    def type(self):
        print("Usa is a developed country")
obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()