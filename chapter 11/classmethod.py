class Employee:
    company = " Camel "
    salary = 100
    location = "delhi"

    # def changeSalary(self, sal):
    #     self._class_.salary = sal

    @classmethod
    def changeSalary(cls,sal):
        cls.salary = sal

e = Employee()
print(e.salary)    
e.changeSalary(455)
print(e.salary)
print(Employee.salary)