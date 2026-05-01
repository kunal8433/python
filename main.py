import random
'''
r for rock
p for paper
s fro seasor

'''
print("WELCOME TO KUNAL MALIK GAME !")
print()
computer = random.choice([1,2,3])
maindict = {1:"rock",2:"paper",3:"seasor"}

yourstr = input("Enter your choice r/p/s :")
yourdict = {"r":1,"p":2,"s":3}

you = yourdict[yourstr]

print(f"The choice of compuer is {maindict[computer]} \n your choice is {maindict[you]}")

if computer == you:
    print("Draw")
else:
    if computer == 1 and you == 2 :
        print("You Win!")
    elif computer == 1 and you == 3:
        print("You Loss!")
    elif computer == 2 and you == 1 :
        print("You Loss!")
    elif computer == 2 and you == 3:
        print("You Win!")
    elif computer == 3 and you == 1 :
        print("You Win!")
    elif computer == 3 and you == 2:
        print("You Loss!")
    else :
        print("ERROR")
        



