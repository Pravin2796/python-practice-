# f = open ('sample.txt','w')
# f.write('add in file')
# f.close()

#appending is used to add content into file 

# f = open("sample.txt","w")
# f.write("this is nice")
# f.close()

with open ('sample.txt','r') as f:
    a = f.read()
    print(a)