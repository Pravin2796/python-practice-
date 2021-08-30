class Employee:
    company= "google"

harry = Employee()
rajni = Employee()
harry.salary = 300
rajni.salary = 400
print(harry.company)
print(rajni.company)
Employee.company = "youtube"
print(harry.company)
print(rajni.company)
print(harry.salary)
print(rajni.salary)
