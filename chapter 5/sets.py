#a = {1,2,5,6}
#set doennt print repetative elements
#a{} will create empty dict not set
b=set()
#print(type(b))
b.add(2)#cannot ad list and dict in set elements
print(len(b)) # print the length of b

b.remove(2) # emove 2 fom b
b.pop()

print(b)