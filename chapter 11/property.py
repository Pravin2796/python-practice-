class Employee:
    company = " bharta gas"
    salary = 4500
    bonus = 500

    @property
    def totalsalary(self):
        return self.salary + self.bonus

    @totalsalary.setter
    def totalsalary(self, val):
        self.bonus = val - self.salary
e = Employee()
print(e.totalsalary)        
e.totalsalary = 5580
print(e.salary)
print(e.bonus)