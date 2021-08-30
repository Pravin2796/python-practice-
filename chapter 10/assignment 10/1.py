class Programmer:
    company =" microsoft"
    def __init__(self,name ,product):
        self.name = name
        self.product = product
    def getDetails(self):
        print(f"the name of the coder is {self.name} and the product is {self.product}")


harry = Programmer("harry","skype")
Pravin = Programmer("Pravin","GitHub")
harry.getDetails()
Pravin.getDetails()        