class Employee:
    company = "Google"

    def showDetails(self):
        print("this is an employee")

class Programmer(Employee):
    language = 'python'
    company = " yot tube"

    def getLanguage(self):
        print(f"the language is {self.language}")

    def showDetails(self):
        print("this is an programmer")

a = Employee()
a.showDetails()
p = Programmer()
p.showDetails()
print(p.company)

