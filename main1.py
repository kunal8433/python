import random

'''
r for rock 
p for paper
s for scissor

'''

computer = random.choice([1,2,3])
youstr = input("Enter your choice :")

maindint = {1:"rock" , 2: "paper" ,3:"scissor"}
youdict = {"r":1 , "p":2 ,"s" :3}

you = youdict[youstr] 

if you == computer:
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
# i hope you like it