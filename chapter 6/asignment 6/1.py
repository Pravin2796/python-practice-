num1 = input("enter no 1")
num2 = input("enter no 2")
num3 = input("enter no 3")
num4 = input("enter no 4")

if(num1 > num4):
    f1 = num1
else:
    f1 = num4

if(num2 > num3):
    f2 = num2
else:
    f2 = num3
if(f1>f2):
    print(str(f1) + "is greater")
else:
    print(str(f2) + "is greater")                 