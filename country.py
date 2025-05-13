class India():
    def capital(self):
        print("capital of ind=New Delhi")
    def language(self):
        print("language of ind=Hindi")
    def type(self):
        print("India is a developing country")
class USA():
    def capital(self):
        print("capital of usa=Washington, DC")
    def language(self):
        print("language of usa=English")
    def type(self):
        print("USA is a developed country")
ob1=India()
ob2=USA()

for country in (ob1, ob2):
    country.capital()
    country.language()
    country.type()
       