class Employee:
    company = " google"
    def getSalary(self,signature):
        print(f"salary for this employee working in {self.company} is {self.salary}")
    @staticmethod
    def greet():
        print("good morning, sir!!")
harry = Employee()
harry.salary = 10000
harry.getSalary("Thanx")
harry.greet()