class Employee:
    company = "google"

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        print("employee is created!")
    def getDetails(self):
        print(f"the name of the employee is{self.name}")
        print(f"the salary of the employee is{self.salary}")

                 
harry = Employee("harry",100)        
harry.getDetails()