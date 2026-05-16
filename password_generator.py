import random as rn


def passwd():
        word ="abcdefghjiklmnopqrstuvwxyz"
        upword="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        bd = "!@#$%^&*"
        

        print(rn.choice(upword) + rn.choice(bd) + rn.choice(bd)+ rn.choice(upword) + rn.choice(word) + rn.choice(upword) + rn.choice(bd) + rn.choice(upword) + str(rn.randint(1,101)) + rn.choice(word) + str(rn.randint(1,101)) + rn.choice(word) + rn.choice(upword) + rn.choice(upword) + str(rn.randint(1,101)))
i = int(input("How many strong passwords you wanna get? "))
for sayi in range(i):
        passwd()
