import random as rn 


def passwd():
        word ="abcdefghjiklmnopqrstuvwxyz"    #digits for random to choice 
        upword="ABCDEFGHIJKLMNOPQRSTUVWXYZ"     #capslock digits for random to choice
        bd = "!@#$%^&*"         #idk either
        print(rn.choice(upword) + rn.choice(bd) + rn.choice(bd)+ rn.choice(upword) + rn.choice(word) + rn.choice(upword) + rn.choice(bd) + rn.choice(upword) + str(rn.randint(1,101)) + rn.choice(word) + str(rn.randint(1,101)) + rn.choice(word) + rn.choice(upword) + rn.choice(upword) + str(rn.randint(1,101)))
        #this prints passwords generates 18 character long passwords

i = int(input("How many strong passwords you wanna get? ")) #how many passwd u want 
for u in range(i):
        passwd()

        
