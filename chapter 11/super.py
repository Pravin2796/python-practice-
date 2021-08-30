class Person:
    country = " india"

    def takeBreath(self):
        print("i am brearthing...")

class Employee(Person):
    company = "honda"

    def getSalary(self):
        print(f"salary is {self.salary}")

    def takeBreath(self):
        print("i am an employee so i luckiely breathing")

class Programmer(Employee):
    company = "fiverr" 

    def getSalary(self):
        print(f"No Salary to programmer")
    def takeBreath(self):
        super().takeBreath()
        print("i am a programmer ")

p = Person()
#p.takeBreath()
e = Employee()
#e.takeBreath()
pr = Programmer() 
pr.takeBreath() 
print(pr.company)                 
