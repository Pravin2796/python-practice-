class Employee:
    company = "google"
    salary = 100

harry = Employee()
rajni = Employee()

# creating instance attribute salary for both objects
harry.salary = 300
# rajni.salary = 400

print(harry.salary)
print(rajni.salary)