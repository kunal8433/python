import random
'''
s for snake 
w for water
g for gun

'''
computer = random.choice([1,2,3])
you = input("Enter your choice:")
yourdict = {"s":1, "w":2 , "g":3}
maindict = {1:"snake" , 2 : "water" , 3 : "gun"}

yournumber = yourdict [you]

print(f"your choice {maindict[yournumber]} ,/n computer choice {maindict[computer]}")

if yournumber == computer:
    print("Match Draw!")
else:
    if you == 1 and  computer == 2 :
        print("You Win!")
    elif you == 1 and  computer == 3 :
        print("You loss!")
    elif you == 2 and  computer == 3 :
        print("You loss!")
    elif you == 2 and  computer == 1 :
        print("You Win!")
    elif you == 3 and  computer == 1 :
        print("You Win!")
    elif you == 3 and  computer == 2 :
        print("You loss!")
    else:
        print("Something went wrong!")
