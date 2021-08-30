class Employee:
    company = " google "
    def getSalary(self): #
        print(f"salary for this employee working in {self.company} is {self.salary}")
harry = Employee()
harry.salary = 10000
harry.getSalary() #Employee.getSalary(harry)
       