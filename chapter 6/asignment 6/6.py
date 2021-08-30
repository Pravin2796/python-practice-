marks = int(input("enter the marks\n"))

if marks>=90:
    grade = "excl"
elif marks>=80:
    grade = "A"
elif marks>=70:
    grade = "B"

else:
    grade = "F" 
print("your grade is " + grade)               