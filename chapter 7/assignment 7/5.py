num = int(input("enter the no : \n"))
if num < 0:
     print("enter positive no")
else:
     sum = 0    
while (num>0):
    sum += num 
    num -= 1
print("total is : ",sum)    
