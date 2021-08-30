def percent(marks):
    p = (sum(marks)/400)*100
    return p

marks1 = [45,50,60,25]
percentage1 = percent(marks1) 

marks2 = [35,61,80,64]
percentage2 = percent(marks2)

print(percentage1,percentage2)  