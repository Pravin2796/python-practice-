sub1 = int(input("enter 1st sub marks\n"))
sub2 = int(input("enter 2st sub marks\n"))
sub3 = int(input("enter 3st sub marks\n"))

if(sub1<33 or sub2<33 or sub3<33):
    print("ypu are fail in one sub")
elif(sub1+sub2+sub3)/3 < 40:
    print("you are failed")
else:
    print("you are passed")        