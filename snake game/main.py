import random
# snake water gun or rock paper sessor
def gamewin(comp,you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True 
    elif comp == 'w':
        if you == 'g': 
            return False
        elif you == 's':
            return True
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True    
print("comp Turn: Snake(s) water(w) or gun(g)?" )
randno = random.randint(1,3)
if randno == 1:
    comp = 's'
elif randno == 2:
    comp = 'w'
elif randno == 3:
    comp = 'g'

you = input("your Turn: Snake(s) water(w) or gun(g)?")
a = gamewin(comp,you)    

print(f"computer chose {comp}")
print(f"you chose {you}")
if a == None:
    print("game is a tie!")
elif a:
    print("you win!")
else:
    print("you lose")        
