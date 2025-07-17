class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    
    def showdetails(self):
        print(f"the name of emplyoee{self.id}is {self.name}")

class programer(employee):
    # def __init__(self,language):
        # self.language=language
    def showlanguage(self,language):
        self.langauge=language
        print(f"language used by {self.name} is {self.langauge}")

e=employee("tanishq",567)
e.showdetails()
e1=programer("don",420)
e1.showdetails()
e1.showlanguage("C")

