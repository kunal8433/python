import random

'''
1 for gun
2 for water
3 for snake 

'''

computer = random.choice([1,2,3])
yourstr = input("Enter your choice :")
yourdict = { "g":1 , "w":2 , "s" :3 }
maindict= {1:"gun",2:"w",3:"snake"}

you = yourdict [yourstr]

print(f"your choice {maindict[you]} |and| computer choice {maindict[computer]} ")

if computer == you :
    print("MATCH DRAW!")

else :
    if computer == 1 and you == 1 :
        print("YOU WIN !")
    elif computer == 1 and you == 2 :
        print("YOU loss !")
    elif computer == 1 and you == 3 :
        print("YOU loss !")
    elif computer == 3 and you == 2 :
        print("YOU loss !")
    elif computer == 2 and you == 3 :
        print("YOU loss !")
    elif computer == 1 and you == 1 :
        print("YOU loss !")
    elif computer == 3 and you == 2 :
        print("YOU loss !")
    elif computer == 2 and you == 1 :
        print("YOU loss !")
    else:
        print("error")

